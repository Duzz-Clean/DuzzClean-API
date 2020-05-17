# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from model import Backend
app = Flask(__name__)
backend = Backend()


#mostrar json de motoristas - FUNCIONANDO
@app.route('/veiculos', methods=['GET'])
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
@app.route('/veiculos/<string:placa>', methods=['DELETE'])
def excluir_carro(placa):
    pass


#excluir usuario - FUNCIONANDO
@app.route('/usuarios/<int:cpf>', methods=['DELETE'])
def excluir_usuario(cpf):
    pass



#adicionar novo motorista - FUNCIONANDO
@app.route('/veiculos', methods=['POST'])
def save_motorista():
    data = request.get_json()
    response = backend.novo_veiculo(data)
    status = int(response['status'])
    return jsonify(data), status


#adicionar novo usuario - FUNCIONANDO
@app.route('/usuarios', methods=['POST'])
def save_usuario():
    data = request.get_json()
    response = backend.novo_usuario(data)
    status = int(response['status'])
    return jsonify(response), status



#pesquisar por placa - FUNCIONANDO
@app.route('/veiculos/<string:placa>', methods=['GET'])
def por_placa(placa):
    pass

#pesquisar por ultima limpeza - ACHO QUE NÃO TEM NECESSIDADE, PQ QUANDO PESQUISAR POR PLACA JÁ VAI TER ESSE DADO (FUNCIONANDO)
@app.route('/veiculos/ultima_limpeza/<string:ultima_limpeza>', methods=['GET'])
def ultimalimpeza(ultima_limpeza):
    pass


#usuario solicita nova limpeza - FUNCIONANDO
@app.route('/nova_limpeza', methods=['POST'])
def nova_limpeza():
    data = request.get_json()
    response = backend.nova_limpeza(data)
    status = int(response['status'])
    return jsonify(data), status


#avalicao do cliente a respeito de UM carro(QRcode) - FUNCIONANDO
@app.route('/nova_avaliacao', methods=['POST'])
def avaliacao():
    data = request.get_json()
    response = backend.nova_avaliacao(data)
    status = int(response['status'])
    return jsonify(response), status


@app.route ('/recusa_notificacao', methods=['POST'])
def recusa_notificacao():
    data = request.json()
    response = backend.recusa_notificacao(data)
    status = int(response['status'])
    return jsonify(data), status

@app.route ('/grava_envio_notificao', methods=['POST'])
def grava_envio_notificao():
    data = request.json()
    response = backend.grava_envio_notificao(data)
    status = int(response['status'])
    return jsonify(data), status

@app.route ('/solicitar_limpeza', methods=['POST'])
def solicitar_limpeza():
    data = request.json()
    response = backend.solicitar_limpeza(data)
    status = int(response['status'])
    return jsonify(data), status

@app.route ('/autenticar_usuario', methods=['POST'])
def autenticar_usuario():
    data = request.json()
    response = backend.autenticar_usuario(data)
    status = int(response['status'])
    return jsonify(data), status

@app.route ('/buscar_notificacoes', methods=['POST'])
def buscar_notificacoes():
    data = request.json()
    response = backend.buscar_notificacoes(data)
    status = int(response['status'])
    return jsonify(data), status


if __name__ == "__main__":
    app.run(debug=True)

# FALTANDO JONAS FAZER NO ARQUIVO "model.py" A FUNÇÃO DE NOVO VEICULO