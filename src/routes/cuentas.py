from flask import Blueprint, jsonify, request
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
@main.route('/crear_cuenta', methods=['POST'])
def crear_cuenta():
    try:
        nombre = request.json['nombre']
        saldo = request.json['saldo']
        num_cuenta = request.json['cuenta']
        telefono = request.json['telefono']
        id = uuid.uuid4()
        cuenta_nueva = cuentas(str(id), nombre, saldo, telefono, num_cuenta)
        estado = cuentas_model.crear_cuenta(cuenta_nueva)
        if estado == 1:
            return jsonify({'status': 'ok', 'data':cuenta_nueva.cuenta})
        else:
            return jsonify({'message': "Error on insert"}), 500
    except Exception as ex:
      return jsonify({'message':str(ex).split(' ')}), 500
@cross_origin() 
@main.route('/consignar/<id>', methods=['PUT'])
def consignar(id):
    try:
        saldo = request.json['saldo']
        consignacion = {'id':id, 'saldo':saldo}
        estado = cuentas_model.consignar(consignacion)
        if estado == 1:
            return jsonify({'status': 'ok', 'data': consignacion['id']})
        else:
            return jsonify({'message': "Error on update"}), 500
    except Exception as ex:
      return jsonify({'message':str(ex)}), 500
@cross_origin()
@main.route('/retirar/<id>', methods=['PUT'])
def retirar(id):
    try:
        monto = request.json['monto']
        retiro = {'id':id, 'monto':monto}
        estado = cuentas_model.retirar(retiro)
        if estado == 1:
            return jsonify({'status': 'ok', 'data': 1, 'message': 'Retiro exitoso'})
        elif estado == 0:
            return jsonify({'status': 'ok', 'data': 0, 'message': 'Saldo insuficiente'})
        else:
            return jsonify({'message': "Error on update "}), 500
    except Exception as ex:
      return jsonify({'message':str(ex)}), 500