#encoding utf-8

#__author__ = Jonas Duarte, duarte.jsystem@gmail.com
#Python3
__author__ = 'Jonas Duarte'
import random
import string
import hashlib
from mysql_manager import Gera_query
from database_manager import Database
from controller import Controller
from random import randint


class Backend():
    def __init__(self):
        self.database = Database()
        self.gera_query = Gera_query()
        self.controller = Controller()


    def gera_salt(self):
        letras = string.ascii_uppercase

        for x in range(0, 100):
            salt = ''.join(random.choice(letras) for _ in range(3))
            salt += str(randint(0,9))
            salt += ''.join(random.choice(letras) for _ in range(3))

        return salt


    def novo_usuario(self, data):
        try:
            login = data['Login']
            password = data['Password']
            first_name = data['FirstName']
            second_name = data['SecondName']
            user_type   = data['UserType']

            salt = self.gera_salt()

            password = hashlib.md5(str(password + salt).encode())
            password = password.hexdigest()


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
