from decimal import Decimal
from database.db import get_connection
from .entities.cuentas import cuentas


class cuentas_model():

    @classmethod
    def get_cuentas(self):
        try:
            con = get_connection()
            cuentas_list = []
            try:
                with con.cursor() as cursor:
                  query = "SELECT * FROM cuentas_ahorros"
                  # values = (cuenta_id,)
                  cursor.execute(query,)
                  # resultado = cursor.fetchone()
                  resultado = cursor.fetchall()
                  # return resultado
                  for row in resultado:
                      cuenta = cuentas(row[0], row[1], row[2], row[3], row[4])
                      cuentas_list.append(cuenta.to_JSON())
                  con.close()
                  return cuentas_list
            except Exception as ex:
                raise Exception(ex)
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def consultar_cuenta(self, id):
        try:
            con = get_connection()
            with con.cursor() as cursor:
                query = 'SELECT * FROM cuentas_ahorros WHERE cuenta = %s'
                values = (id,)
                cursor.execute(query,values)
                row = cursor.fetchone()
                cuenta = None;
                if row != None:
                    cuenta = cuentas(row[0], row[1], row[2], row[3], row[4])
                    cuenta = cuenta.to_JSON()
                con.close()
                return cuenta

        except Exception as ex:
           raise Exception(ex)
    
    @classmethod
    def crear_cuenta(self, cuenta_nueva):
        try:
            con = get_connection()
            with con.cursor() as cursor:
                query = 'INSERT INTO cuentas_ahorros (nombre, cuenta, saldo, telefono) VALUES (%s, %s, %s, %s)'
                values = (cuenta_nueva.nombre, cuenta_nueva.cuenta, cuenta_nueva.saldo, cuenta_nueva.telefono)
                cursor.execute(query, values)
                filas_afectadas = cursor.rowcount
                con.commit()
            con.close()
            return filas_afectadas
        except Exception as ex:
          print(ex) 
          raise Exception(ex)
        
    @classmethod
    def consignar(self, valor_cuenta):
        print(valor_cuenta)
        try:
            con = get_connection()
            with con.cursor() as cursor:
                query = 'UPDATE cuentas_ahorros SET saldo = saldo+%s WHERE cuenta = %s'
                values = (valor_cuenta['saldo'], valor_cuenta['id'])
                cursor.execute(query, values)
                filas_afectadas = cursor.rowcount
                con.commit()
            con.close()
            return filas_afectadas
        except Exception as ex:
           raise Exception(ex)
    
    @classmethod
    def retirar(self, valor_monto):
        try:
            saldo = self.consultar_cuenta(valor_monto['id'])
            saldo_actual = int(Decimal(saldo['saldo']))
            if  saldo_actual < int(valor_monto['monto']):
              return 0
            con = get_connection()
            with con.cursor() as cursor:
                id = valor_monto['id']
                query = 'UPDATE cuentas_ahorros SET saldo = saldo-%s WHERE cuenta = %s'
                values = (valor_monto['monto'], valor_monto['id'])
                cursor.execute(query, values)
                filas_afectadas = cursor.rowcount
                con.commit()
            con.close()
            return filas_afectadas
        except Exception as ex:
           raise Exception(ex)
             
