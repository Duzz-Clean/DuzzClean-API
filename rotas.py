#encoding utf-8

#__author__ = Pablo Mariz, souzamariz27@gmail.com
#Python3

from flask import Flask, jsonify, request
from model import Backend
app = Flask(__name__)
backend = Backend()

#adicionar novo motorista - FUNCIONANDO
@app.route('/novo_veiculo', methods=['POST'])
def novo_veiculo():
    try:
        data = request.get_json()
        if len(data) > 4:
            raise Exception('Request out of params')

        response = backend.confirm_token(data)
        if response['Message'] != 'OK':
            raise Exception('Invalid Token')
            
        response = backend.novo_veiculo(data)
    except Exception as e:
        response = {
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        }

    status = int(response['Status'])
    return jsonify(response), 200

#adicionar novo usuario - FUNCIONANDO
@app.route('/novo_usuario', methods=['POST'])
def novo_usuario():
    try:
        data = request.get_json()

        if len(data) > 5:
            raise Exception('Request out of params')

        response = backend.novo_usuario(data)

    except Exception as e:
        response = {
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        }
    status = int(response['Status'])
    return jsonify(response), 200

#usuario solicita nova limpeza - FUNCIONANDO
@app.route('/nova_limpeza', methods=['POST'])
def nova_limpeza():
    try:
        data = request.get_json()
        if len(data) > 5:
            raise Exception('Request out of params')


        response = backend.confirm_token(data)
        if response['Message'] != 'OK':
            raise Exception('Invalid Token')
            
        response = backend.nova_limpeza(data)

    except Exception as e:
        response = {
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        }
    status = int(response['Status'])
    return jsonify(response), 200

#avalicao do cliente a respeito de UM carro(QRcode) - FUNCIONANDO
@app.route('/nova_avaliacao', methods=['POST'])
def nova_avaliacao():
    try:
        data = request.get_json()
        if len(data) > 6:
            raise Exception('Request out of params')


        response = backend.confirm_token(data)
        if response['Message'] != 'OK':
            raise Exception('Invalid Token')

        response = backend.nova_avaliacao(data)
 
 
    except Exception as e:
        response = {
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        }
    status = int(response['Status'])
    return jsonify(response), 200


@app.route ('/recusa_notificacao', methods=['POST'])
def recusa_notificacao():
    try:
        data = request.get_json()
        if len(data) > 6:
            raise Exception('Request out of params')


        response = backend.confirm_token(data)
        if response['Message'] != 'OK':
            raise Exception('Invalid Token')
            
        response = backend.recusa_notificacao(data)

    except Exception as e:
        response = {
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        }
    status = int(response['Status'])
    return jsonify(response), 200


@app.route ('/grava_envio_notificao', methods=['POST'])
def grava_envio_notificao():
    try:
        data = request.get_json()
        if len(data) > 4:
            raise Exception('Request out of params')


        response = backend.confirm_token(data)
        if response['Message'] != 'OK':
            raise Exception('Invalid Token')
            
        response = backend.grava_envio_notificao(data)
        
    except Exception as e:
        response = {
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        }
    status = int(response['Status'])
    return jsonify(response), 200


@app.route ('/solicitar_limpeza', methods=['POST'])
def solicitar_limpeza():
    try:
        data = request.get_json()
        if len(data) > 5:
            raise Exception('Request out of params')


        response = backend.confirm_token(data)
        if response['Message'] != 'OK':
            raise Exception('Invalid Token')
            
        response = backend.solicitar_limpeza(data)
    
    except Exception as e:
        response = {
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        }
    status = int(response['Status'])
    return jsonify(response), 200


@app.route ('/autenticar_usuario', methods=['POST'])
def autenticar_usuario():
    try:
        data = request.get_json()
        if len(data) > 3:
            raise Exception('Request out of params')


        response = backend.autenticar_usuario(data)

    except Exception as e:
        response = {
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        }
    status = int(response['Status'])
    return jsonify(response), 200   


@app.route ('/buscar_notificacoes', methods=['POST'])
def buscar_notificacoes():
    try:
        data = request.get_json()
        if len(data) > 3:
            raise Exception('Request out of params')


        response = backend.confirm_token(data)
        if response['Message'] != 'OK':
            raise Exception('Invalid Token')
            
        response = backend.buscar_notificacoes(data)

    except Exception as e:
        response = {
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        }
    status = int(response['Status'])
    return jsonify(response), 200


@app.route ('/buscar_limpezas_veiculo', methods=['POST'])
def buscar_limpezas_veiculo():
    try:
        data = request.get_json()
        if len(data) > 4:
            raise Exception('Request out of params')

        response = backend.confirm_token(data)
        if response['Message'] != 'OK':
            raise Exception('Invalid Token')
            
        response = backend.buscar_limpezas_veiculo(data)
        
    except Exception as e:
        response = {
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        }
    status = int(response['Status'])
    return jsonify(response), 200


@app.route ('/buscar_resumo_veiculo', methods=['POST'])
def buscar_resumo_veiculo():
    try:
        data = request.get_json()
        if len(data) > 4:
            raise Exception('Request out of params')


        response = backend.confirm_token(data)
        if response['Message'] != 'OK':
            raise Exception('Invalid Token')
            
        response = backend.buscar_resumo_veiculo(data)

    except Exception as e:
        response = {
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        }
    status = int(response['Status'])
    return jsonify(response), 200


@app.route ('/buscar_ultima_limpeza_veiculo', methods=['POST'])
def buscar_ultima_limpeza_veiculo():
    try:
        data = request.get_json()
        if len(data) > 4:
            raise Exception('Request out of params')


        response = backend.confirm_token(data)
        if response['Message'] != 'OK':
            raise Exception('Invalid Token')
            
        response = backend.buscar_ultima_limpeza_veiculo(data)

    except Exception as e:
        response = {
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        }
    status = int(response['Status'])
    return jsonify(response), 200


@app.route ('/buscar_limpeza', methods=['POST'])
def buscar_limpeza():
    try:
        data = request.get_json()
        if len(data) > 4:
            raise Exception('Request out of params')


        response = backend.confirm_token(data)
        if response['Message'] != 'OK':
            raise Exception('Invalid Token')
            
        response = backend.buscar_limpeza(data)

    except Exception as e:
        response = {
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        }
    status = int(response['Status'])
    return jsonify(response), 200


@app.route ('/realizar_logoff', methods=['POST'])
def realizar_logoff():
    try:
        data = request.get_json()
        if len(data) > 4:
            raise Exception('Request out of params')


        response = backend.confirm_token(data)
        if response['Message'] != 'OK':
            raise Exception('Invalid Token')
            
        response = backend.realizar_logoff(data)

    except Exception as e:
        response = {
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        }
    status = int(response['Status'])
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(debug=True)
