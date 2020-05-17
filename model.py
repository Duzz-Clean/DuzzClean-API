#encoding utf-8

#__author__ = Jonas Duarte, duarte.jsystem@gmail.com
#Python3
__author__ = 'Jonas Duarte'
import random
import string
import hashlib
import pyqrcode
from mysql_manager import Gera_query
from database_manager import Database
from controller import Controller
from random import randint


class Backend():
    def __init__(self):
        self.database = Database()
        self.gera_query = Gera_query()
        self.controller = Controller()


    def gera_qrcode(self, license_plate):
        qr_code = pyqrcode.create(license_plate)
        path = f'qrCodes/{license_plate}.png'
        qr_code.png(path, scale=10)

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
            login = data['Username']
            password = data['Password']
            first_name = data['FirstName']
            second_name = data['SecondName']
            user_type   = data['UserType']

            salt = self.gera_salt()

            password = self.crypto(password, salt)

            columns = self.database.return_columns('usuarios')
            columns.pop('id')
            dados = [login, first_name, second_name, '', password, salt, user_type]

            query = self.gera_query.inserir_na_tabela('usuarios', columns, dados, string=True)

            self.database.commit_without_return(query)

            self.r = {
                'message' : 'OK',
                'status'  : 200
            }

        except Exception as e:
            self.r = {
                'message' : {
                    'error' : str(e)
                },
                'status' : 401
            }

        return self.r

    
    def novo_veiculo(self, data):
        try:
            license_plate = data['LicensePlate']
            username = data['Username']

            user_id = self.database.return_user_id(username)
            columns = self.database.return_columns('carros')
            codigo_qr = self.gera_qrcode(license_plate)

            dados = ['Null', f'"{license_plate}"', f'"{codigo_qr}"', user_id]

            query = self.gera_query.inserir_na_tabela('carros', columns, dados)
            self.database.commit_without_return(query)

            self.r = {
                'message' : 'OK',
                'status'  : 200
            }
    
        except Exception as e:
            self.r = {
                'message' : {
                    'error' : str(e)
                },
                'status' : 400
            }

        return self.r

    def nova_limpeza(self, data):
        try:
            license_plate = data['LicensePlate']
            date = data['Date']
            birth_type = data['BirthType']
            km = data['Km']
            clean_type = data['CleanType']

            car_id = self.database.return_car_id(license_plate)
            columns = self.database.return_columns('limpezas')

            values = [
                car_id,
                date,
                km,
                birth_type,
                clean_type
            ]

            query = self.gera_query.inserir_na_tabela('limpezas', list(columns.keys()), values)
            self.database.commit_without_return(query)

            self.r = {
                'message' : 'OK',
                'status'  : 200
            }
    
        except Exception as e:
            self.r = {
                'message' : {
                    'error' : str(e)
                },
                'status' : 400
            }

        return self.r


    def nova_manutencao(self, data):
        try:
            license_plate = data['LicensePlate']
            type = data['Type']
            date = data['Date']
            date_future = ['NextTime']

            car_id = self.database.return_car_id(license_plate)
            columns = self.database.return_columns('limpezas_geral')
            values = car_id
            values.append([x for x in list(data.values())[1:]])

            query = self.gera_query.inserir_na_tabela('manutencoes', list(columns.keys()), values)
            self.database.commit_without_return(query)

            self.r = {
                'message' : 'OK',
                'status'  : 200
            }
        except Exception as e:
            self.r = {
                'message' : {
                    'error' : str(e)
                },
                'status' : 400
            }

        return self.r


    def grava_envio_notificao(self, data):
        try:
            notificacao_id = data['NotificationId']
            
            query = self.gera_query.alterar_dados_da_tabela('notificacoes', ['enviada'], ['TRUE'], 
                where=True, valor_where=notificacao_id, coluna_verificacao='id')

            self.database.commit_without_return(query)

            self.r = {
                'message' : 'OK',
                'status'  : 200
            }
        except Exception as e:
            self.r = {
                'message' : {
                    'error' : str(e)
                },
                'status' : 400
            }

        return self.r

    def recusa_notificacao(self, data):
        try:
            license_plate = data['LicensePlate']
            date = data['Date']
            km = data['Km']
        
            columns = self.database.return_columns('notificacoes_recusas')
            car_id = self.database.return_car_id(license_plate)
            values = car_id
            values.append([x for x in list(data.values())[1:]])
            query = self.gera_query.inserir_na_tabela('notificacoes_recusadas', columns, [car_id, date, km])

            self.database.commit_without_return(query)

            self.r = {
                'message' : 'OK',
                'status'  : 200
            }
        except Exception as e:
            self.r = {
                'message' : {
                    'error' : str(e)
                },
                'status' : 400
            }

        return self.r


    def nova_avaliacao(self, data):
        try:
            license_plate = data['LicensePlate']
            rating = data['Rating']
            comment = data['Comment']

            car_id = self.database.return_car_id(license_plate)
            columns = self.database.return_columns('carros_satisfactions')

            query = self.gera_query.inserir_na_tabela('carros_satisfacao', columns, [car_id, rating, comment])
            self.database.commit_without_return(query)

            self.r = {
                'message' : 'OK',
                'status'  : 200
            }

        except Exception as e:
            self.r = {
                'message' : {
                    'error' : str(e)
                },
                'status' : 400
            }

        return self.r


    def solicitar_limpeza(self, data):
        try:
            license_plate = data['LicensePlate']
            requesting_user = data['RequestingUser']
            
            car_id = self.database.return_car_id(license_plate)

            query = self.gera_query.inserir_na_tabela('notificacoes', ['carro', 'tipo', 'usuario'], [car_id, 0, requesting_user])    
            
            self.database.commit_without_return(query)

            self.r = {
                'message' : 'OK',
                'status'  : 200
            }
        except Exception as e:
            self.r = {
                'message' : {
                    'error' : str(e)
                },
                'status' : 400
            }
        
        return self.r


    def autenticar_usuario(self, data):
        try:
            username = data['Username']
            password = data['Password']

            
            salt = self.database.return_salt(username)

            password = self.crypto(password, salt)

            response = self.compare_password(username, password)

            if response:
                self.r = {
                    'message' : 'OK',
                    'status'  : 200
                }
            else:
                self.r = {
                    'message' : {
                        'error' : 'incorrect username or password'
                    },
                    'status'  : 404
                }
        except Exception as e:
            self.r = {
                    'message' : {
                        'error' : str(e)
                    },
                    'status'  : 404
                }
        return self.r


    def buscar_notificacoes(self, data):
        try:
            username = data['Username']

            user_id = self.database.return_user_id(username)

            notifications = self.database.return_notifications(user_id)

            self.r = {
                'message' : notifications,
                'status'  : 200
            }
        except Exception as e:
            self.r = {
                    'message' : {
                        'error' : str(e)
                    },
                    'status'  : 404
                }
        return self.r

    
    def buscar_limpezas_veiculo(self, data):
        try:
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
                'message' : limpezas,
                'status'  : 200
            }
        except Exception as e:
            self.r = {
                    'message' : {
                        'error' : str(e)
                    },
                    'status'  : 404
                }
        return self.r
    
    def buscar_resumo_veiculo(self, data):
        try:
            license_plate = data['LicensePlate']

            car_id = self.database.return_car_id(license_plate)


            informacoes = self.database.return_resume_of_vehicle(car_id)

            self.r = {
                'message' : informacoes,
                'status'  : 200
            }
        except Exception as e:
            self.r = {
                    'message' : {
                        'error' : str(e)
                    },
                    'status'  : 404
                }
        return self.r


    def buscar_ultima_limpeza_veiculo(self, data):
        try:
            license_plate = data['LicensePlate']

            car_id = self.database.return_car_id(license_plate)

            query = f'select limpezas.id, limpezas.data from limpezas where carro={car_id} order by limpezas.id desc limit 1'

            response = self.database.commit_with_return(query)[0]

            ultima_limpeza = {
                'LimpezaId' : response[0],
                'LimpezaData' : response[1]
            }
            self.r = {
                'message' : ultima_limpeza,
                'status'  : 200
            }
        except Exception as e:
            self.r = {
                    'message' : {
                        'error' : str(e)
                    },
                    'status'  : 404
                }
        return self.r


    def buscar_limpeza(self, data):
        try:
            limpeza_id = data['LimpezaId']

            query = f'select data from limpezas where id = {limpeza_id}'
            limpeza = self.database.commit_with_return(query)[0][0]

            self.r = {
                'message' : limpeza,
                'status'  : 200
            }
        except Exception as e:
            self.r = {
                    'message' : {
                        'error' : str(e)
                    },
                    'status'  : 404
                }
        return self.r
        
