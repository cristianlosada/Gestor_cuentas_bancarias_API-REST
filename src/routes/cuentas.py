from flask import Blueprint, jsonify, request, make_response
from flask_cors import CORS, cross_origin
import uuid


# Entities
from models.entities.cuentas import cuentas
# Modelos
from models.cuentas_model import cuentas_model

main = Blueprint('cuentas_blueprint', __name__)
CORS(main)
@cross_origin()
@main.route('/')
def get_cuentas():
    try:
        cuentas = cuentas_model.get_cuentas()
        return jsonify({'status': 'ok', 'data':cuentas})
    except Exception as ex:
      return jsonify({'message': str(ex)}), 500
    
@cross_origin()
@main.route('/<id>')
def consultar_cuenta(id):
    try:
        cuenta = cuentas_model.consultar_cuenta(id)
        if cuenta != None: 
          return jsonify({'status': 'ok', 'data':cuenta})
        else:
          return jsonify({'status': 'ok', 'data':{}})
    except Exception as ex:
      return jsonify({'message': str(ex)}), 500
@cross_origin()
@main.route('/crear_cuenta', methods=['POST','OPTIONS'])
def crear_cuenta():
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response
    try:
        nombre = request.json['nombre']
        saldo = request.json['saldo']
        num_cuenta = request.json['cuenta']
        telefono = request.json['telefono']
        id = uuid.uuid4()
        cuenta_nueva = cuentas(str(id), nombre, saldo, telefono, num_cuenta)
        estado = cuentas_model.crear_cuenta(cuenta_nueva)
        print(estado)
        if estado == 1:
            return jsonify({'status': 'ok', 'data':1})
        elif estado == 0:
            return jsonify({'status': 'ok', 'data':0})
        else:
            return jsonify({'message': "Error on insert"}), 500
    except Exception as ex:
      return jsonify({'status': 'ok', 'data':int(str(ex).split(' ')[0])})
@cross_origin() 
@main.route('/consignar/<id>', methods=['PUT', 'OPTIONS'])
def consignar(id):
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response
    try:
        saldo = request.json['saldo']
        consignacion = {'id':id, 'saldo':saldo}
        estado = cuentas_model.consignar(consignacion)
        if estado['filas'] == 1:
            return jsonify({'status': 'ok', 'data': estado})
        elif estado['filas'] == 0:
           return jsonify({'status': 'ok', 'data': estado, 'message': 'No existe cuenta'})
        else:
            return jsonify({'message': "Error on update"}), 500
    except Exception as ex:
      return jsonify({'message':str(ex)}), 500
@cross_origin()
@main.route('/retirar/<id>', methods=['PUT', 'OPTIONS'])
def retirar(id):
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response
    try:
        monto = request.json['monto']
        retiro = {'id':id, 'monto':monto}
        estado = cuentas_model.retirar(retiro)
        if estado['filas'] == 1:
            return jsonify({'status': 'ok', 'data': estado, 'message': 'Retiro exitoso'})
        elif estado['filas'] == 3:
            return jsonify({'status': 'ok', 'data': estado, 'message': 'Saldo insuficiente'})
        elif estado['filas'] == 0:
            return jsonify({'status': 'ok', 'data': estado, 'message': 'No existe cuenta'})
        else:
            return jsonify({'message': "Error on update "}), 500
    except Exception as ex:
      return jsonify({'message':str(ex)}), 500