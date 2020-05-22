#encoding utf-8

#__author__ = Jonas Duarte, duarte.jsystem@gmail.com
#Python3
__author__ = 'Jonas Duarte'

import random
import string
import hashlib
import pyqrcode
from os import system
from mysql_manager import Gera_query
from database_manager import Database
from controller import Controller
from random import randint


class Backend():
    def __init__(self):
        self.database = Database()
        self.gera_query = Gera_query()
        self.controller = Controller()


    def gera_token(self, data):
        try:
            user_type = data['UserType']
            username = data['Username']

            user_id = self.database.return_user_id(username)

            token = str(user_type)
            token += self.crypto(username, str(user_id))

            query = f"INSERT INTO `tokens` (`user`,`token`) VALUES ({user_id}, '{token}');"
            self.database.commit_without_return(query, database = 2)

            self.r = {
                'Message' : token,
                'Status'  : 200
            }
        except Exception as e:

            self.r = {
                    'Message' : {
                        'Error' : str(e)
                    },
                    'Status'  : 404
                }
        return self.r


    def search_token(self, user_id):
        try:
            query = f'select token from tokens where user = {user_id}' 
            token = self.database.commit_with_return(query)[0][0]

        except:
            raise Exception('User ID não possui token')

        return token

    
    def confirm_token(self, data):
        try:            
            token = data['Token']
            username = data['Username']
            user_type = data['UserType']

            user_id = self.database.return_user_id(username)

            v_token = str(user_type)
            v_token += self.crypto(username, user_id)

            query = f'select user from tokens where token = {token}'
            user_token = self.database.commit_with_return(query, database = 2)[0][0]

            if v_token == token and user_token == user_id:
                self.r = {
                    'Message' : 'OK',
                    'Status'  : 200
                }
            else:
                raise Exception('Invalid credencials')
        except Exception as e:
            self.r = {
                'Message' : {
                    'error' : str(e)
                },
                'Status' : 401
            }
        return self.r


    def active_token(self, token, user_id):
        try:
            query = f'select id from tokens where token = {token} and user = {user_id}'
            token_id = self.database.commit_with_return(query, database = 2)[0]
        
            if len(token_id) > 0:
                query = self.gera_query.alterar_dados_da_tabela('connections', ['active'], [1], where=True, 
                    valor_where=token_id[0], coluna_verificacao='id')
                self.database.commit_without_return(query, database = 2)
            else:
                query = self.gera_query.inserir_na_tabela('connections', ['token'], [token_id[0]])
                self.database.commit_without_return(query, database = 2)
            
            self.r = {
                'Message' : {
                    'token' : token,
                    'token_id' : token_id[0]
                },
                'Status'  : 200
            }
        except Exception as e:
            self.r = {
                'Message' : {
                    'Error' : str(e)
                },
                'Status'  : 404
            }


    def deactive_token(self, token):
        try:
            query = f'select id from tokens where token = {token}'
            token_id = self.database.commit_with_return(query, database = 2)[0]
            
            if len(token_id) > 0:
                query = self.gera_query.alterar_dados_da_tabela('connections', ['active'], [0], where=True, 
                    valor_where=token_id[0], coluna_verificacao='id')
                self.database.commit_without_return(query, database = 2)
            else:
                query = self.gera_query.inserir_na_tabela('connections', ['token', 'active'], [token_id[0], 0])
                self.database.commit_without_return(query, database = 2)
            
            self.r = {
                'Message' : 'OK',
                'Status'  : 200
            }
        except Exception as e:
            self.r = {
                'Message' : {
                    'Error' : str(e)
                },
                'Status'  : 404
            }


    def gera_qrcode(self, license_plate):
        qr_code = pyqrcode.create(license_plate)
        path = f'qrCodes/{license_plate}.png'
        try:
            qr_code.png(path, scale=10)
        except Exception as e:
            print(e)
            system('mkdir qrCodes')
            self.gera_qrcode(license_plate)

        return path


    def gera_salt(self):
        letras = string.ascii_uppercase

        for x in range(0, 100):
            salt = ''.join(random.choice(letras) for _ in range(3))
            salt += str(randint(0,9))
            salt += ''.join(random.choice(letras) for _ in range(3))

        return salt


    def compare_password(self, username, password):
        passw = self.database.return_password(username, password)

        if passw == password:
            return True
        else:
            return False


    def crypto(self, password, salt):
        password = hashlib.md5(str(password + salt).encode())
        password = password.hexdigest()

        return password


    def novo_usuario(self, data):
        try:
            username = data['Username']
            password = data['Password']
            first_name = data['FirstName']
            second_name = data['SecondName']
            user_type   = data['UserType']

            salt = self.gera_salt()

            password = self.crypto(password, salt)

            columns = self.database.return_columns('usuarios')
            columns.pop('id')
            dados = [username, first_name, second_name, '', password, salt, user_type]

            query = self.gera_query.inserir_na_tabela('usuarios', columns, dados, string=True)

            self.database.commit_without_return(query)

            token = self.gera_token(data)

            self.r = {
                'Message' : {
                        'Username' : username,
                        'FirstName' : first_name,
                        'SecondName' : second_name,
                        'UserType' : user_type,
                        'Token' : token
                },
                'Status'  : 200
            }

        except Exception as e:
            self.r = {
                'Message' : {
                    'Error' : str(e)
                },
                'Status' : 401
            }

        return self.r

    
    def novo_veiculo(self, data):
        try:
            username = data['Username']
            user_type = data['UserType']
            license_plate = data['LicensePlate']

            user_id = self.database.return_user_id(username)
            columns = self.database.return_columns('carros')
            codigo_qr = self.gera_qrcode(license_plate)

            dados = ['Null', f'"{license_plate}"', f'"{codigo_qr}"', user_id]

            query = self.gera_query.inserir_na_tabela('carros', columns, dados)
            self.database.commit_without_return(query)

            self.r = {
                'Message' : 'OK',
                'Status'  : 200
            }
    
        except Exception as e:
            self.r = {
                'Message' : {
                    'Error' : str(e)
                },
                'Status' : 400
            }

        return self.r

    def nova_limpeza(self, data):
        try:
            username = data['Username']
            user_type = data['UserType']
            license_plate = data['LicensePlate']
            date = data['Date']

            car_id = self.database.return_car_id(license_plate)
            columns = self.database.return_columns('limpezas')

            values = [
                'Null',
                car_id,
                date
            ]

            query = self.gera_query.inserir_na_tabela('limpezas', list(columns.keys()), values)
            self.database.commit_without_return(query)

            self.r = {
                'Message' : 'OK',
                'Status'  : 200
            }
    
        except Exception as e:
            self.r = {
                'Message' : {
                    'Error' : str(e)
                },
                'Status' : 400
            }

        return self.r


    def grava_envio_notificao(self, data):
        try:
            username = data['Username']
            user_type = data['UserType']
            notificacao_id = data['NotificationId']
            
            query = self.gera_query.alterar_dados_da_tabela('notificacoes', ['enviada'], ['TRUE'], 
                where=True, valor_where=notificacao_id, coluna_verificacao='id')

            self.database.commit_without_return(query)

            self.r = {
                'Message' : 'OK',
                'Status'  : 200
            }
        except Exception as e:
            self.r = {
                'Message' : {
                    'Error' : str(e)
                },
                'Status' : 400
            }

        return self.r

    def recusa_notificacao(self, data):
        try:
            username = data['Username']
            user_type = data['UserType']
            license_plate = data['LicensePlate']
            date = data['Date']
            notificacao_id = data["NotificationId"]
        
            columns = self.database.return_columns('notificacoes_recusas')
            car_id = self.database.return_car_id(license_plate)
            values = ['Null', notificacao_id, 1, car_id, date]
            query = self.gera_query.inserir_na_tabela('notificacoes_recusadas', columns, values)

            self.database.commit_without_return(query)

            self.r = {
                'Message' : 'OK',
                'Status'  : 200
            }
        except Exception as e:
            self.r = {
                'Message' : {
                    'Error' : str(e)
                },
                'Status' : 400
            }

        return self.r


    def nova_avaliacao(self, data):
        try:
            username = data['Username']
            user_type = data['UserType']
            license_plate = data['LicensePlate']
            rating = data['Rating']
            comment = data['Comment']

            car_id = self.database.return_car_id(license_plate)
            columns = self.database.return_columns('carros_satisfactions')
            values = ['Null', car_id, rating, comment]
            query = self.gera_query.inserir_na_tabela('carros_satisfacao', columns, values)
            self.database.commit_without_return(query)

            self.r = {
                'Message' : 'OK',
                'Status'  : 200
            }

        except Exception as e:
            self.r = {
                'Message' : {
                    'Error' : str(e)
                },
                'Status' : 400
            }

        return self.r


    def solicitar_limpeza(self, data):
        try:
            username = data['Username']
            user_type = data['UserType']
            license_plate = data['LicensePlate']
            username = data['Username']
            
            user_id = self.database.return_user_id(username)
            car_id = self.database.return_car_id(license_plate)

            query = self.gera_query.inserir_na_tabela('notificacoes', ['carro', 'tipo', 'usuario'], [car_id, 0, username])    
            
            self.database.commit_without_return(query)

            self.r = {
                'Message' : 'OK',
                'Status'  : 200
            }
        except Exception as e:
            self.r = {
                'Message' : {
                    'Error' : str(e)
                },
                'Status' : 400
            }
        
        return self.r


    def autenticar_usuario(self, data):
        try:
            username = data['Username']
            user_type = data['UserType']
            password = data['Password']

            user_id = self.database.return_user_id(username)

            if not user_id:
                raise Exception('Usuário não encontrado no banco de dados')

            token = self.search_token(user_id)

            if len(token) == 0:
                raise Exception('User ID não possui token')
            
            salt = self.database.return_salt(username)

            password = self.crypto(password, salt)

            response = self.compare_password(username, password)

            if response:
                query = f'select first_name, second_name, photo_path from usuarios where id = {user_id}'
                first_name, second_name, photo_path = self.database.commit_with_return(query)[0]
                

                self.active_token(token, user_id)
                self.r = {
                    'Message' : {
                        'Username' : username,
                        'UserType' : user_type,
                        'FirstName' : first_name,
                        'SecondName' : second_name,
                        'PhotoPath'  : photo_path,
                        'Token' : token
                    },
                    'Status'  : 200
                }
            else:
                self.r = {
                    'Message' : {
                        'Error' : 'incorrect username or password'
                    },
                    'Status'  : 404
                }
        except Exception as e:
            self.r = {
                    'Message' : {
                        'Error' : str(e)
                    },
                    'Status'  : 404
                }
        return self.r


    def realizar_logoff(self, data):
        try:
            username = data['Username']
            user_type = data['UserType']
            token = data['Token']

            self.deactive_token(token)

            self.r = {
                'Message' : 'OK'
            }
        except Exception as e:
            self.r = {
                'Message' : {
                    'Error' : str(e)
                },
                'Status' : 200
            }


    def buscar_notificacoes(self, data):
        try:
            username = data['Username']
            user_type = data['UserType']

            user_id = self.database.return_user_id(username)

            notifications = self.database.return_notifications(user_id)

            self.r = {
                'Message' : notifications,
                'Status'  : 200
            }
        except Exception as e:
            self.r = {
                    'Message' : {
                        'Error' : str(e)
                    },
                    'Status'  : 404
                }
        return self.r

    
    def buscar_limpezas_veiculo(self, data):
        try:
            username = data['Username']
            user_type = data['UserType']
            license_plate = data['LicensePlate']

            car_id = self.database.return_car_id(license_plate)

            query = f'select * from limpezas where carro = {car_id}'
            response = self.database.commit_with_return(query)

            limpezas = {
                
            }

            for limpeza in response:
                limpezas[f'Limpeza{limpeza[0]}'] = {
                    'ID' : limpeza[0],
                    'CarId' : limpeza[1],
                    'LicensePlate' : license_plate,
                    'DateTime' : limpeza[2]
                }

            self.r = {
                'Message' : limpezas,
                'Status'  : 200
            }
        except Exception as e:
            self.r = {
                    'Message' : {
                        'Error' : str(e)
                    },
                    'Status'  : 404
                }
        return self.r
    
    def buscar_resumo_veiculo(self, data):
        try:
            username = data['Username']
            user_type = data['UserType']
            license_plate = data['LicensePlate']

            car_id = self.database.return_car_id(license_plate)


            informacoes = self.database.return_resume_of_vehicle(car_id)

            self.r = {
                'Message' : informacoes,
                'Status'  : 200
            }
        except Exception as e:
            self.r = {
                    'Message' : {
                        'Error' : str(e)
                    },
                    'Status'  : 404
                }
        return self.r


    def buscar_ultima_limpeza_veiculo(self, data):
        try:
            username = data['Username']
            user_type = data['UserType']
            license_plate = data['LicensePlate']

            car_id = self.database.return_car_id(license_plate)

            query = f'select limpezas.id, limpezas.data from limpezas where carro={car_id} order by limpezas.id desc limit 1'

            response = self.database.commit_with_return(query)[0]

            ultima_limpeza = {
                'LimpezaId' : response[0],
                'LimpezaData' : response[1]
            }
            self.r = {
                'Message' : ultima_limpeza,
                'Status'  : 200
            }
        except Exception as e:
            self.r = {
                    'Message' : {
                        'Error' : str(e)
                    },
                    'Status'  : 404
                }
        return self.r


    def buscar_limpeza(self, data):
        try:
            username = data['Username']
            user_type = data['UserType']
            limpeza_id = data['LimpezaId']

            query = f'select data from limpezas where id = {limpeza_id}'
            limpeza = self.database.commit_with_return(query)[0][0]

            self.r = {
                'Message' : limpeza,
                'Status'  : 200
            }
        except Exception as e:
            self.r = {
                    'Message' : {
                        'Error' : str(e)
                    },
                    'Status'  : 404
                }
        return self.r
        

    def buscar_resumo_usuario(self, data):
        try:
            username = data['Username']
            user_type = data['UserType']
            user_id = self.database.return_user_id(username)

            query = 'select type, first_name, second_name from usuarios where id = ' + str(user_id)
            user_type, first_name, second_name = self.database.commit_with_return(query)[0]

            usuario = {
                'Username' : username,
                'UserId'   : user_id,
                'UserType' : user_type,
                'FirstName': first_name,
                'SecondName': second_name
            }
            self.r = {
                'Message' : usuario,
                'Status'  : 200
            }
        except Exception as e:
            self.r = {
                    'Message' : {
                        'Error' : str(e)
                    },
                    'Status'  : 404
                }
        return self.r
