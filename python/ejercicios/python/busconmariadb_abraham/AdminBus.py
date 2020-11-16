import mysql.connector
from Conexion import cur

class AdminBus:
        
    def insertBus(self,objbus):
        rows_count = 0
        sql = """INSERT INTO bus(
            nombre, numero_plazas, plazas_disponibles, plazas_vendidas)
            VALUES (%s, %s, %s, %s);"""
        try:
            cur.execute(sql, (objbus.getNombre(), objbus.getPlazas(), objbus.getPlazas(), 0))
            rows_count = cur.rowcount
        except mysql.connector.Error as error:
            print(error)

        return rows_count
    
    def showBus(self,nombre):
        sql = "select * from bus where nombre = %s"
        try:
            cur.execute(sql, (nombre,))
            bus = cur.fetchall()
        except mysql.connector.Error as error:
            print(error)
        
        return bus


    def showBuses(self):
        sql = "SELECT * FROM bus"
        try:
            cur.execute(sql)
            buses = cur.fetchall()
        except mysql.connector.Error as error:
            print(error)
        
        return buses


    def mostrarPasajeros(self,nombre):
        sql = """SELECT p.dni, p.nombre, p.apellido, p.direccion, t.cantidad_billetes, t.fecha_compra
            FROM pasajero as p
            JOIN transaccion as t ON p.dni=t.dni_pasajero
            JOIN bus as b ON t.nombre_bus=b.nombre
            WHERE b.nombre LIKE %s"""
        try:
            cur.execute(sql,(nombre,))
            pasajeros = cur.fetchall()
        except mysql.connector.Error as error:
            print(error)
        
        return pasajeros

    def updatePlazasDisponibles(self,plazasDisponibles,nombre):
        sql = """UPDATE bus SET plazas_disponibles = (%s) WHERE nombre = (%s)""" 
        try:
            cur.execute(sql,(plazasDisponibles, nombre))
            rows_set = cur.rowcount
        except mysql.connector.Error as error:
            print(error)
        
        return rows_set


    def updatePlazasVendidas(self,plazasVendidas,nombre):
        sql = """UPDATE bus SET plazas_vendidas = (%s) WHERE nombre = (%s)""" 
        try:
            cur.execute(sql,(plazasVendidas, nombre))
            rows_set = cur.rowcount
        except mysql.connector.Error as error:
            print(error)
        
        return rows_set
    
    

    def deleteBus(self,nombre):
        sql = "DELETE FROM bus WHERE nombre = %s"
        try:
            cur.execute(sql, (nombre,))
            rows_deleted = cur.rowcount
        except mysql.connector.Error as error:
            print(error)
        
        return rows_deleted
    

    def deleteTransaccionBus(self,nombrebus):
        sql = """DELETE FROM transaccion WHERE nombre_bus LIKE %s""" 
        try:
            cur.execute(sql,(nombrebus,))
            rows_deleted = cur.rowcount
        except  mysql.connector.Error as error:
            print(error)
        
        return rows_deleted

    def comprobarTransaccionBus(self,nombrebus):
        sql = "select * from transaccion where nombre_bus = %s"
        try:
            cur.execute(sql, (nombrebus,))
            transaccion = cur.fetchall()
        except  mysql.connector.Error as error:
            print(error)
        
        return transaccion
