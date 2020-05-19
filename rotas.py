#encoding utf-8

#__author__ = Pablo Mariz, souzamariz27@gmail.com
#Python3

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
@app.route('/novo_veiculo', methods=['POST'])
def novo_veiculo():
    data = request.get_json()
    response = backend.novo_veiculo(data)
    status = int(response['status'])
    return jsonify(response), status


#adicionar novo usuario - FUNCIONANDO
@app.route('/novo_usuario', methods=['POST'])
def novo_usuario():
    data = request.get_json()
    response = backend.novo_usuario(data)
    status = int(response['status'])
    return jsonify(response), status



#usuario solicita nova limpeza - FUNCIONANDO
@app.route('/nova_limpeza', methods=['POST'])
def nova_limpeza():
    data = request.get_json()
    response = backend.nova_limpeza(data)
    status = int(response['status'])
    return jsonify(response), status

#avalicao do cliente a respeito de UM carro(QRcode) - FUNCIONANDO
@app.route('/nova_avaliacao', methods=['POST'])
def nova_avaliacao():
    data = request.get_json()
    response = backend.nova_avaliacao(data)
    status = int(response['status'])
    return jsonify(response), status


@app.route ('/recusa_notificacao', methods=['POST'])
def recusa_notificacao():
    data = request.json()
    response = backend.recusa_notificacao(data)
    status = int(response['status'])
    return jsonify(response), status

@app.route ('/grava_envio_notificao', methods=['POST'])
def grava_envio_notificao():
    data = request.json()
    response = backend.grava_envio_notificao(data)
    status = int(response['status'])
    return jsonify(response), status

@app.route ('/solicitar_limpeza', methods=['POST'])
def solicitar_limpeza():
    data = request.json()
    response = backend.solicitar_limpeza(data)
    status = int(response['status'])
    return jsonify(response), status

@app.route ('/autenticar_usuario', methods=['POST'])
def autenticar_usuario():
    data = request.json()
    response = backend.autenticar_usuario(data)
    status = int(response['status'])
    return jsonify(response), status

@app.route ('/buscar_notificacoes/<string:username>', methods=['GET'])
def buscar_notificacoes(username):
    data = request.get_json()
    response = backend.buscar_notificacoes(data)
    status = int(response['status'])
    return jsonify(response), status

@app.route ('/buscar_limpezas_veiculo/<string:license_plate>', methods=['GET'])
def buscar_limpezas_veiculo(license_plate):
    data = request.get_json()
    response = backend.buscar_limpezas_veiculo(data)
    status = int(response['status'])
    return jsonify(response), status

@app.route ('/buscar_resumo_veiculo/<string:license_plate>', methods=['GET'])
def buscar_resumo_veiculo(license_plate):
    data = request.get_json()
    response = backend.buscar_resumo_veiculo(data)
    status = int(response['status'])
    return jsonify(response), status

@app.route ('/buscar_ultima_limpeza_veiculo/<string:license_plate>', methods=['GET'])
def buscar_ultima_limpeza_veiculo(license_plate):
    data = request.get_json()
    response = backend.buscar_ultima_limpeza_veiculo(data)
    status = int(response['status'])
    return jsonify (response), status

@app.route ('/buscar_limpeza/<string:license_plate>', methods=['GET'])
def buscar_limpeza(license_plate):
    data = request.get_json()
    response = backend.buscar_limpeza(data)
    status = int(response['status'])
    return jsonify (response), status



if __name__ == "__main__":
    app.run(debug=True)
