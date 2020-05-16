# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from model import Backend

app = Flask(__name__)

backend = Backend()

motoristas = [
    {
        'nome': 'Joao Pablo',
        'placa': '123',
        'ultima_limpeza': '20-10',
        'limpezas_recusadas': 3,

        'nova_manutencao':{
            'dia': '10-89',
            'km': '15000'
        }
    },
    {
        'nome': 'Jonas',
        'placa': '1234',
        'ultima_limpeza': '21-10',
        'limpezas_recusadas': 8,

        'nova_manutencao':{
            'dia': '17-9',
            'km': '250'
        }
    }, 
    {
        'nome': 'Matheus',
        'placa': '12345',
        'ultima_limpeza': '20-10',
        'limpezas_recusadas': 2,

        'nova_manutencao':{
            'dia': '7-01',
            'km': '58795'
        }
    }
]

usuarios = [
    {
        'nome': 'diego',
        'cpf': 1
    },
    {
        'nome': 'usuario2',
        'cpf': 2
    }
]

nova_limpeza = [
    {
        'usuario': 1, #cpf do usuario que ta solicitando nova limpeza
        'carro': '123ijk', #placa do carro que ta recebendo a solicitação
        'aceito': 'true' #boolen no bd pra aceitar ou nao a limpeza <3
    },
    {
        'usuario': 2,
        'carro': '584',
        'aceito': 'false'
    }
]

avaliacao_do_usuario = [ #avaliação do usuario a respeito de UM UNICO carro
    {
        'usuario': 2, #cpf usuario ou algo q o identifica
        'carro': '4897s', #placa do carro ou algo q o identifica
        'avaliacao': 'UMA BOSTA' #avaliacao do cliente
    }
]


#mostrar json de motoristas - FUNCIONANDO
@app.route('/motoristas', methods=['GET'])
def home_motoristas():
    pass

#mostrar json de usuarios - FUNCIONANDO
@app.route('/usuarios', methods=['GET'])
def home_usuarios():
    pass

#mostrar json de limpezas solicitadas - FUNCIONANDO
@app.route('/nova_limpeza', methods=['GET'])
def home_nova_limpeza():
    pass

#mostrar json de avaliacao do usuario a respeito de UM UNIICO carro - FUNCIONANDO 
@app.route('/avaliacao_do_usuario', methods=['GET'])
def home_avalicao():
    pass

#excluir carro - FUNCIONANDO
@app.route('/motoristas/<string:placa>', methods=['DELETE'])
def excluir_carro(placa):
   pass

#excluir usuario - FUNCIONANDO
@app.route('/usuarios/<int:cpf>', methods=['DELETE'])
def excluir_usuario(cpf):
    pass

#adicionar novo usuario - FUNCIONANDO
@app.route('/usuarios', methods=['POST'])
def save_usuario():
    data = request.get_json()
    
    response = backend.novo_usuario(data)
    
    status = int(response['status'])
 
    return jsonify(data), status

#pesquisar por placa - FUNCIONANDO
@app.route('/motoristas/<string:placa>', methods=['GET'])
def por_placa(placa):
    pass

#pesquisar por ultima limpeza - ACHO QUE NÃO TEM NECESSIDADE, PQ QUANDO PESQUISAR POR PLACA JÁ VAI TER ESSE DADO (FUNCIONANDO)
@app.route('/motoristas/ultima_limpeza/<string:ultima_limpeza>', methods=['GET'])
def ultimalimpeza(ultima_limpeza):
    pass

#usuario solicita nova limpeza - FUNCIONANDO
@app.route('/nova_limpeza', methods=['POST'])
def solicitacao_limpeza():
    pass

#avalicao do cliente a respeito de UM carro(QRcode) - FUNCIONANDO
@app.route('/avaliacao_do_usuario', methods=['POST'])
def avaliacao():
    pass

#pesquisar situação do carro, e sua proxima manutenção.
@app.route('/motoristas/nova_manutencao/<string:placa>', methods=['GET'])
def nova_manutencao(placa):
    pass

if __name__ == "__main__":
    app.run(debug=True)