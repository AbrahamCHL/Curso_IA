import mysql.connector
from Conexion import cur

class AdminPasajero:

    def insertPasajero(self,objpasajero):
        rows_count = 0
        sql = """INSERT INTO pasajero(
            dni, apellido, nombre, direccion)
            VALUES (%s, %s, %s, %s);"""
        try:
            cur.execute(sql, (objpasajero.getDni(),objpasajero.getNombre(), objpasajero.getApellido(), objpasajero.getDireccion()))
            rows_count = cur.rowcount
        except mysql.connector.Error as error:
            print(error)

        return rows_count
    

    def showPasajero(self,dni):
        sql = "select * from pasajero where dni = %s"
        try:
            cur.execute(sql, (dni,))
            pasajero = cur.fetchall()
        except mysql.connector.Error as error:
            print(error)
        
        return pasajero


    def showPasajeros(self):
        sql = "SELECT * FROM pasajero"
        try:
            cur.execute(sql)
            pasajeros = cur.fetchall()
        except mysql.connector.Error as error:
            print(error)
        
        return pasajeros

    def deletePasajero(self,dni):
        sql = "DELETE FROM pasajero WHERE dni = %s"
        try:
            cur.execute(sql, (dni,))
            rows_deleted = cur.rowcount
        except mysql.connector.Error as error:
            print(error)
        
        return rows_deleted
    
    def deleteTransaccionPasajero(self,dni):
        sql = """DELETE FROM transaccion WHERE dni_pasajero LIKE %s""" 
        try:
            cur.execute(sql,(dni,))
            rows_deleted = cur.rowcount
        except  mysql.connector.Error as error:
            print(error)
        
        return rows_deleted


    def comprobarTransaccionPasajero(self,dni):
        sql = "select * from transaccion where dni_pasajero = %s"
        try:
            cur.execute(sql, (dni,))
            transaccion = cur.fetchall()
        except  mysql.connector.Error as error:
            print(error)
        
        return transaccion