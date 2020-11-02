import psycopg2
from Conexion import cur
class Transaccion:
    def __init__(self):
        pass
    

    def comprarBilletes(self,dni_pasajero,nombre_bus,billetesAcomprar):
        rows_count = 0
        sql = """INSERT INTO transaccion(
            nombre_bus, dni_pasajero, cantidad_billetes)
            VALUES (%s, %s, %s);"""
        try:
            cur.execute(sql, (nombre_bus, dni_pasajero, billetesAcomprar))
            rows_count = cur.rowcount
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return rows_count
    

    def devolverBilletes(self,dni_pasajero,nombre_bus,billetesAdevolver):
        rows_set = 0
        billetescomprados = self.comprobarTransaccion(nombre_bus,dni_pasajero)[0][3]
        billetescomprados -= billetesAdevolver

        sql = """UPDATE transaccion SET cantidad_billetes = %s WHERE dni_pasajero like %s and nombre_bus = %s""" 
        try:
            cur.execute(sql,(billetescomprados, dni_pasajero,nombre_bus))
            rows_set = cur.rowcount
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        return rows_set


    def updateTransaccion(self,dni_pasajero,nombre_bus,billetesAcomprar):
        rows_set = 0
        billetescomprados = self.comprobarTransaccion(nombre_bus,dni_pasajero)[0][3]
        billetesAcomprar += billetescomprados

        sql = """UPDATE transaccion SET cantidad_billetes = %s WHERE dni_pasajero like %s and nombre_bus = %s""" 
        try:
            cur.execute(sql,(billetesAcomprar, dni_pasajero,nombre_bus))
            rows_set = cur.rowcount
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        return rows_set

    def comprobarTransaccion(self,nombre_bus, dni_pasajero):
        sql = "select * from transaccion where nombre_bus = %s and dni_pasajero = %s"
        try:
            cur.execute(sql, (nombre_bus, dni_pasajero))
            transaccion = cur.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        return transaccion

    def showTransaccion(self,dni_pasajero):
        sql = "select * from transaccion where dni_pasajero = %s"
        try:
            cur.execute(sql, (dni_pasajero,))
            transaccion = cur.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        return transaccion

    def comprobarBusDelPasajero(self,nombre_bus,dni_pasajero):
        sql = "select * from transaccion where dni_pasajero = %s and nombre_bus = %s"
        try:
            cur.execute(sql, (dni_pasajero,nombre_bus))
            transaccion = cur.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        return transaccion

   
