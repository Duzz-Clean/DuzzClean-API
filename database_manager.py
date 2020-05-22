#encoding utf-8

#__author__ = Jonas Duarte, duarte.jsystem@gmail.com
#Python3

import MySQLdb as mdb
import configparser
from mysql_manager import Gera_query

class Database():
    def __init__(self):
        self.gerador_de_query = Gera_query()
        self.connected = False


    def connect(self, database):
        if not self.connected:
            credencials = self.authenticate(database)
            address = credencials.get('AddressBank')
            name = credencials.get('NameBank')
            user = credencials.get('UserBank')
            password = credencials.get('PasswordBank')
        
            try:
                self.bank = mdb.connect(address, user, password, name)
            except:
                self.conected = False
                raise
            else:
                self.cursor = self.bank.cursor()
                self.conected = True

        return {
            'Database' : self.bank,
            'Cursor'   : self.cursor
        }
    
    def disconnect(self):
        if self.connected:
            try:
                self.bank.close()
            except:
                raise Exception('Database connection not initialized')
        
        self.conected = False
        return True

    def authenticate(self, database):
        """
        Utiliza as informações presentes no glpi.cfg para\n
        retorná-las em forma de lista como credenciais
        Retorno -> Lista:\n
        [0] IP banco, [1] Usuario Banco\n
        [2] Senha Usuario, [3] Nome Banco
        """
        config = configparser.ConfigParser()
        config.read('conf.cfg')

        if database == 1:
            config_bank = 'config_bank_app'
        else:
            config_bank = 'config_bank_api'

        print(config_bank)

        address_bank = config.get(config_bank, 'address_bank')
        name_bank = config.get(config_bank, 'name_bank')
        user_bank = config.get(config_bank, 'user_bank')
        password_bank = config.get(config_bank, 'password_bank')
        if password_bank == "''":
            password_bank = ''

        return {
            'AddressBank' : address_bank,
            'NameBank' : name_bank,
            'UserBank' : user_bank,
            'PasswordBank' : password_bank
        }


    def commit_without_return(self, query, database = 1):
        self.connect(database)
        try:
            self.cursor.execute(query)
        except:
            raise
        else:
            self.bank.commit()
            self.disconnect()
            return True

    def commit_with_return(self, query, database = 1):
        results = None
        self.connect(database)
        try:
            self.cursor.execute(query)
        except:
            raise
        else:
            results = self.cursor.fetchall()
            self.disconnect()

        return results


    def return_columns(self,  table):
        query = self.gerador_de_query.listar_colunas(table)
        columns = self.commit_with_return(query)
        dict_columns = {

        }

        for column in columns:
            dict_columns[column[0]] = [column[x+1] for x in range(len(column[1:]))]

        return dict_columns


    def return_car_id(self, license_plate):
        query = self.gerador_de_query.search_car_id(license_plate)

        car_id = self.commit_with_return(query)[0][0]

        return car_id


    def return_user_id(self, username):
        query = f'select id from usuarios where username = "{username}"'

        user_id = self.commit_with_return(query)[0][0]

        return user_id


    def return_salt(self, username):
        query = f'select salt from usuarios where username = "{username}"'

        salt = self.commit_with_return(query)[0][0]

        return salt


    def return_password(self, username, password):
        query = f'select password from usuarios where username = "{username}" and password = "{password}"'

        password = self.commit_with_return(query)[0][0]

        return password

    
    def return_notifications(self, user_id):
        query = 'select carros.placa, notificacoes_tipos.descricao, corpo from notificacoes '
        query += 'inner join carros on notificacoes.carro = carros.id '
        query += 'inner join notificacoes_tipos on notificacoes.tipo = notificacoes_tipos.id '
        query += f'where enviada = False and notificacoes.usuario = {user_id} '
        

        notifications = {

        }
        responses = self.commit_with_return(query)
        
        for response in responses:
            notifications[response[0]] = [response[x+1] for x in range(len(response[1:]))]

        return notifications

    
    def return_resume_of_vehicle(self, car_id):
        query = 'select AVG(carros_satisfacoes.satisfacao) as "Média de Satisfação", COUNT(DISTINCT(limpezas.id)) as '
        query += '"Limpezas Realizadas", COUNT(DISTINCT(notificacoes.id)) as "Notificações Recebidas", '
        query += 'COUNT(DISTINCT(notificacoes_recusadas.notificacao)) as "Notificações Recusadas" '
        query += 'from carros '
        query += 'inner join carros_satisfacoes on carros.id=carros_satisfacoes.carro '
        query += 'inner join limpezas on carros.id=limpezas.carro '
        query += 'inner join notificacoes on carros.id=notificacoes.carro '
        query += 'inner join notificacoes_recusadas on carros.id=notificacoes_recusadas.carro '
        query += f'where carros.id = {car_id} and notificacoes.enviada = True and '
        query += f'notificacoes.tipo = 1 and notificacoes_recusadas.tipo = 1'

        response_db = self.commit_with_return(query)[0]
        info_vehicle = {
            'MediaSatisfação' : response_db[0],
            'LimpezasRealizadas' : response_db[1],
            'NotificacoesRecebidas' : response_db[2],
            'NotificacoesRecusadas' : response_db[3]
        }

        return info_vehicle
