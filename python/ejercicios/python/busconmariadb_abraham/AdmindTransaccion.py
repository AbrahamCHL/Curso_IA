import mysql.connector
from Conexion import cur

class AdminTransaccion:
    
    def comprarBilletes(self,transaccion):
        rows_count = 0
        sql = """INSERT INTO transaccion(
            nombre_bus, dni_pasajero, cantidad_billetes)
            VALUES (%s, %s, %s);"""
        try:
            cur.execute(sql, (transaccion.getNombreBus(), transaccion.getDniPasajero(), transaccion.getBilletesAcomprar()))
            rows_count = cur.rowcount
        except  mysql.connector.Error as error:
            print(error)

        return rows_count
    

    def devolverBilletes(self,transaccion,billetesAdevolver):
        rows_set = 0
        billetescomprados = self.comprobarTransaccion(transaccion)[0][2]
        billetescomprados -= billetesAdevolver
        
        sql = """UPDATE transaccion SET cantidad_billetes = %s WHERE dni_pasajero like %s and nombre_bus = %s""" 
        try:
            cur.execute(sql,(billetescomprados, transaccion.getDniPasajero(),transaccion.getNombreBus()))
            rows_set = cur.rowcount
        except  mysql.connector.Error as error:
            print(error)
        
        return rows_set
         

    def deleteTransaccion(self,transaccion):
        sql = """DELETE FROM transaccion WHERE dni_pasajero LIKE %s and nombre_bus LIKE %s""" 
        try:
            cur.execute(sql,(transaccion.getDniPasajero(),transaccion.getNombreBus()))
        except  mysql.connector.Error as error:
            print(error)

    def updateTransaccion(self,transaccion):
        rows_set = 0
        billetesAcomprar = transaccion.getBilletesAcomprar()
        billetescomprados = self.comprobarTransaccion(transaccion)[0][2]
        billetesAcomprar += billetescomprados

        sql = """UPDATE transaccion SET cantidad_billetes = %s WHERE dni_pasajero like %s and nombre_bus = %s""" 
        try:
            cur.execute(sql,(billetesAcomprar, transaccion.getDniPasajero(),transaccion.getNombreBus()))
            rows_set = cur.rowcount
        except  mysql.connector.Error as error:
            print(error)
        
        return rows_set

    def comprobarTransaccion(self,transaccion):
        sql = "select * from transaccion where nombre_bus = %s and dni_pasajero = %s"
        try:
            cur.execute(sql, (transaccion.getNombreBus(), transaccion.getDniPasajero()))
            transaccion = cur.fetchall()
        except  mysql.connector.Error as error:
            print(error)
        
        return transaccion

    def showTransaccion(self,dni_pasajero):
        sql = "select * from transaccion where dni_pasajero = %s"
        try:
            cur.execute(sql, (dni_pasajero,))
            transaccion = cur.fetchall()
        except  mysql.connector.Error as error:
            print(error)
        
        return transaccion

   
    

   
