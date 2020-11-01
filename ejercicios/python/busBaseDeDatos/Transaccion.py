import psycopg2

class Transaccion:
    def __init__(self):
        pass
    

    def comprarBilletes(self,cursor,dni_pasajero,nombre_bus,billetesAcomprar):
        rows_count = 0
        sql = """INSERT INTO transaccion(
            nombre_bus, dni_pasajero, cantidad_billetes)
            VALUES (%s, %s, %s);"""
        try:
            cursor.execute(sql, (nombre_bus, dni_pasajero, billetesAcomprar))
            rows_count = cursor.rowcount
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return rows_count

    def devolverBilletes(self):
        pass

    def updateTransaccion(self,cursor,dni_pasajero,nombre_bus,billetesAcomprar):
        rows_set = 0
        billetescomprados = self.comprobarTransaccion(cursor,nombre_bus,dni_pasajero)[0][3]
        billetesAcomprar += billetescomprados

        sql = """UPDATE transaccion SET cantidad_billetes = %s WHERE dni_pasajero like %s and nombre_bus = %s""" 
        try:
            cursor.execute(sql,(billetesAcomprar, dni_pasajero,nombre_bus))
            rows_set = cursor.rowcount
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        return rows_set

    def comprobarTransaccion(self,cursor,nombre_bus, dni_pasajero):
        sql = "select * from transaccion where nombre_bus = %s and dni_pasajero = %s"
        try:
            cursor.execute(sql, (nombre_bus, dni_pasajero))
            transaccion = cursor.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        return transaccion

    def showTransaccion(self,cursor,dni_pasajero):
        sql = "select * from transaccion where dni_pasajero = %s"
        try:
            cursor.execute(sql, (dni_pasajero,))
            transaccion = cursor.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        return transaccion

    def comprobarBusDelPasajero(self,cursor,nombre_bus,dni_pasajero):
        sql = "select * from transaccion where dni_pasajero = %s and nombre_bus = %s"
        try:
            cursor.execute(sql, (dni_pasajero,nombre_bus))
            transaccion = cursor.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        return transaccion

    def devolverBilletes(self,cursor,dni_pasajero,nombre_bus,billetesAdevolver):
        rows_set = 0
        billetescomprados = self.comprobarTransaccion(cursor,nombre_bus,dni_pasajero)[0][3]
        billetescomprados -= billetesAdevolver

        sql = """UPDATE transaccion SET cantidad_billetes = %s WHERE dni_pasajero like %s and nombre_bus = %s""" 
        try:
            cursor.execute(sql,(billetescomprados, dni_pasajero,nombre_bus))
            rows_set = cursor.rowcount
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        return rows_set
