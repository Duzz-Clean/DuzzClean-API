#encoding utf-8

#__author__ = Jonas Duarte, duarte.jsystem@gmail.com
#Python3
__author__ = 'Jonas Duarte'

import socketserver
import configparser
import model
import controller
import threading


def Backends():
    return [model.Backend(), controller.Controller()]

 
def BindServer():
    config = configparser.ConfigParser()
    config.read('conf.cfg')

    port = int(config.get('config_server', 'porta'))
    ip = config.get('config_server', 'ip_server')

    server = {
        'ip_address' : ip,
        'server_port' : port
    }
    
    return server
 

class Controller(socketserver.BaseRequestHandler):

    def __init__(self, request, client_address, server):
        self.backends, self.controller = Backends()
        self.request = request
        self.client_address = client_address
        self.server = server
        self.setup()
        try:
            self.handle()
        finally:
            self.finish()


    def handle(self):
        while True:
            # Recebe data do cliente
            lenght_of_data_received = int.from_bytes(self.request.recv(2), byteorder='big')
            data_received = self.request.recv(lenght_of_data_received)
            
            if not data_received: break

            data_received = self.treat_by_separator(data_received)

            request_data = {
                'Request' : self.treat_by_separator(data_received[0], ','),
                'Parameters' : self.treat_by_separator(data_received[1], ',') 
            }

            self.data_send(request_data)
            print('OK')
        print('fechando')
        self.request.close()


    def data_send(self, request_data):
        server_response = self.rigger(request_data).encode()
        lenght_of_response = len(server_response).to_bytes(2, byteorder='big')
        print(server_response)
        self.request.send(lenght_of_response)
        self.request.send(server_response)

        return 'OK'


    def rigger(self, request_data):
        """
        O armador de requisições;
        Função que recebe e solicita 
        a devida info ao backend

        Padrão de requisição: 
        Tipo de request|interface_request   |request
        Entry, or Out  |Motorista or Client | request
        example: E,MOT,LIMPEZA,DADOS;data_nascimento,nascimento,km,tipo,objeto_limpos


        """
        request = request_data.get('Request')
        parameters = request_data.get('Parameters')

        if request[0] == 'E':
            if request[1] == 'MOT':
                if request[2] == 'new_clean':
                    return self.backends.nova_limpeza(parameters[0], parameters[1], parameters[2], parameters[3], parameters[4], parameters[5])
                elif request[2] == 'new_clean_man':
                    return self.backends.nova_manutencao(parameters[0], parameters[1], parameters[2], parameters[3])
                elif request[2] == 'new_refusal':
                    return self.backends.recusa_notificacao(parameters[0], parameters[1], parameters[2])
            elif request[1] == 'CLI':
                if request[2] == 'new_feedback':
                    return self.backends.nova_avaliacao(parameters[0], parameters[1], parameters[2])
        elif request[0] == 'O':
            if request[1] == 'MOT':
                if request[2] == 'view_clean':
                    return self.backends.buscar_limpeza(parameters[0], parameters[1])
                elif request[2] == 'view_geral_clean':
                    return self.backends.buscar_manutencao(parameters[0], parameters[1])
                elif request[2] == 'view_rating':
                    return self.backends.media_avaliacao_carro(parameters[0])
                elif request[2] == 'view_last_clean':
                    return self.backends.ultima_limpeza_realizada(parameters[0])
                elif request[2] == 'view_descuido':
                    return self.backends.media_descuido(parameters[0])
            elif request[1] == 'CLI':
                if request[2] == 'view_rating':
                    return self.backends.media_avaliacao_carro(parameters[0])
                elif request[2] == 'view_last_clean':
                    return self.backends.ultima_limpeza_realizada(parameters[0])
                elif request[2] == 'view_descuido':
                    return self.backends.media_descuido(parameters[0])
        
        return False


    def treat_by_separator(self, request, separator=';'):
        """
        Trata a requisição recebida do cliente.
        Modelo de requisição :
        | TIPO ; PARAMETRO1, PARAMETRO2, ... |
        sendo o ';' separador entre tipo e parametros
        sendo a ',' separador entre os parametros
        
        :return: request[0] = tipo, request[1] = parametros
        """
        try:
            request = request.decode()
        except Exception as e:
            print(e)
        try:
            request = request.split(separator)
        except Exception as e:
            print(e + '\nFunction treat by separator - ' + separator)
        
        return request

 
bind_server = BindServer()

ip = bind_server.get('ip_address')
port = bind_server.get('server_port')

server = socketserver.ThreadingTCPServer((ip, port), Controller)
server.serve_forever()