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
            e = jsonify({
                'Message' : {
                    'Error' : 'Request out of params'
                },
                'Status' : 401
            })
            raise Exception(e)

        response = backend.confirm_token(data)
        if response['Message'] != 'OK':
            raise Exception('Invalid Token')
            
        response = jsonify(backend.novo_veiculo(data))
        status = int(response['status'])

    except Exception as e:
        response = jsonify({
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        })
    return response, status


#adicionar novo usuario - FUNCIONANDO
@app.route('/novo_usuario', methods=['POST'])
def novo_usuario():
    try:
        data = request.get_json()

        if len(data) > 5:
            e = jsonify({
                'Message' : {
                    'Error' : 'Request out of params'
            },
                'Status' : 401
            })
            raise Exception(e)

        response = jsonify(backend.novo_usuario(data))
        status = int(response['status'])
    except Exception as e:
        response = jsonify({
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        })
    return response, status



#usuario solicita nova limpeza - FUNCIONANDO
@app.route('/nova_limpeza', methods=['POST'])
def nova_limpeza():
    try:
        data = request.get_json()
        if len(data) > 5:
            e = jsonify({
                'Message' : {
                    'Error' : 'Request out of params'
                },
                'Status' : 401
            })
            raise Exception(e)

        response = backend.confirm_token(data)
        if response['Message'] != 'OK':
            raise Exception('Invalid Token')
            
        response = jsonify(backend.nova_limpeza(data))
        status = int(response['status'])

    except Exception as e:
        response = jsonify({
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        })
    return response, status



#avalicao do cliente a respeito de UM carro(QRcode) - FUNCIONANDO
@app.route('/nova_avaliacao', methods=['POST'])
def nova_avaliacao():
    try:
        data = request.get_json()
        if len(data) > 6:
            e = jsonify({
                'Message' : {
                    'Error' : 'Request out of params'
                },
                'Status' : 401
            })
            raise Exception(e)

        response = backend.confirm_token(data)
        if response['Message'] != 'OK':
            raise Exception('Invalid Token')

        response = jsonify(backend.nova_avaliacao(data))
        status = int(response['status'])

    except Exception as e:
        response = jsonify({
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        })
    return response, status



@app.route ('/recusa_notificacao', methods=['POST'])
def recusa_notificacao():
    try:
        data = request.get_json()
        if len(data) > 6:
            e = jsonify({
                'Message' : {
                    'Error' : 'Request out of params'
                },
                'Status' : 401
            })
            raise Exception(e)

        response = backend.confirm_token(data)
        if response['Message'] != 'OK':
            raise Exception('Invalid Token')
            
        response = jsonify(backend.recusa_notificacao(data))
        status = int(response['status'])

    except Exception as e:
        response = jsonify({
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        })
    return response, status



@app.route ('/grava_envio_notificao', methods=['POST'])
def grava_envio_notificao():
    try:
        data = request.get_json()
        if len(data) > 4:
            e = jsonify({
                'Message' : {
                    'Error' : 'Request out of params'
                },
                'Status' : 401
            })
            raise Exception(e)

        response = backend.confirm_token(data)
        if response['Message'] != 'OK':
            raise Exception('Invalid Token')
            
        response = jsonify(backend.grava_envio_notificao(data))
        status = int(response['status'])

    except Exception as e:
        response = jsonify({
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        })
    return response, status




@app.route ('/solicitar_limpeza', methods=['POST'])
def solicitar_limpeza():
    try:
        data = request.get_json()
        if len(data) > 5:
            e = jsonify({
                'Message' : {
                    'Error' : 'Request out of params'
                },
                'Status' : 401
            })
            raise Exception(e)

        response = backend.confirm_token(data)
        if response['Message'] != 'OK':
            raise Exception('Invalid Token')
            
        response = jsonify(backend.solicitar_limpeza(data))
        status = int(response['status'])

    except Exception as e:
        response = jsonify({
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        })
    return response, status

@app.route ('/autenticar_usuario', methods=['POST'])
def autenticar_usuario():
    try:
        data = request.json()
        if len(data) > 3:
                e = jsonify({
                    'Message' : {
                        'Error' : 'Request out of params'
                    },
                    'Status' : 401
                })
                raise Exception(e)

        response = jsonify(backend.autenticar_usuario(data))
        status = int(response['status'])

    except Exception as e:
        response = jsonify({
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        })
    return response, status




@app.route ('/buscar_notificacoes/<string:username>', methods=['POST'])
def buscar_notificacoes(username):
    try:
        data = request.get_json()
        if len(data) > 3:
            e = jsonify({
                'Message' : {
                    'Error' : 'Request out of params'
                },
                'Status' : 401
            })
            raise Exception(e)

        response = backend.confirm_token(data)
        if response['Message'] != 'OK':
            raise Exception('Invalid Token')
            
        response = jsonify(backend.buscar_notificacoes(data))
        status = int(response['status'])

    except Exception as e:
        response = jsonify({
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        })
    return response, status



@app.route ('/buscar_limpezas_veiculo/<string:license_plate>', methods=['POST'])
def buscar_limpezas_veiculo(license_plate):
    try:
        data = request.get_json()
        if len(data) > 4:
            e = jsonify({
                'Message' : {
                    'Error' : 'Request out of params'
                },
                'Status' : 401
            })
            raise Exception(e)

        response = backend.confirm_token(data)
        if response['Message'] != 'OK':
            raise Exception('Invalid Token')
            
        response = jsonify(backend.buscar_limpezas_veiculo(data))
        status = int(response['status'])

    except Exception as e:
        response = jsonify({
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        })
    return response, status



@app.route ('/buscar_resumo_veiculo/<string:license_plate>', methods=['POST'])
def buscar_resumo_veiculo(license_plate):
    try:
        data = request.get_json()
        if len(data) > 4:
            e = jsonify({
                'Message' : {
                    'Error' : 'Request out of params'
                },
                'Status' : 401
            })
            raise Exception(e)

        response = backend.confirm_token(data)
        if response['Message'] != 'OK':
            raise Exception('Invalid Token')
            
        response = jsonify(backend.buscar_resumo_veiculo(data))
        status = int(response['status'])

    except Exception as e:
        response = jsonify({
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        })
    return response, status


@app.route ('/buscar_ultima_limpeza_veiculo/<string:license_plate>', methods=['POST'])
def buscar_ultima_limpeza_veiculo(license_plate):
    try:
        data = request.get_json()
        if len(data) > 4:
            e = jsonify({
                'Message' : {
                    'Error' : 'Request out of params'
                },
                'Status' : 401
            })
            raise Exception(e)

        response = backend.confirm_token(data)
        if response['Message'] != 'OK':
            raise Exception('Invalid Token')
            
        response = jsonify(backend.buscar_ultima_limpeza_veiculo(data))
        status = int(response['status'])

    except Exception as e:
        response = jsonify({
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        })
    return response, status


@app.route ('/buscar_limpeza/<string:license_plate>', methods=['POST'])
def buscar_limpeza(license_plate):
    try:
        data = request.get_json()
        if len(data) > 4:
            e = jsonify({
                'Message' : {
                    'Error' : 'Request out of params'
                },
                'Status' : 401
            })
            raise Exception(e)

        response = backend.confirm_token(data)
        if response['Message'] != 'OK':
            raise Exception('Invalid Token')
            
        response = jsonify(backend.buscar_limpeza(data))
        status = int(response['status'])

    except Exception as e:
        response = jsonify({
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        })
    return response, status

@app.route ('/realizar_logoff', methods=['POST'])
def realizar_logoff():
    try:
        data = request.get_json()
        if len(data) > 4:
            e = jsonify({
                'Message' : {
                    'Error' : 'Request out of params'
                },
                'Status' : 401
            })
            raise Exception(e)

        response = backend.confirm_token(data)
        if response['Message'] != 'OK':
            raise Exception('Invalid Token')
            
        response = jsonify(backend.realizar_logoff(data))
        status = int(response['status'])

    except Exception as e:
        response = jsonify({
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 401
        })
    return response, status





if __name__ == "__main__":
    app.run(debug=True)
