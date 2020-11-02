import psycopg2
from Conexion import cur

class Bus:
    def __init__(self):
        pass
        

    def insertBus(self,nombre,numero_plazas ):
        if numero_plazas <0:
            raise Exception("Ha ingresado un numero de plazas negativo, porfavor ingrese un numero positivo")
        
        rows_count = 0
        sql = """INSERT INTO public.bus(
            nombre_bus, numero_plazas, plazas_disponibles, plazas_vendidas)
            VALUES (%s, %s, %s, %s);"""
        try:
            cur.execute(sql, (nombre,numero_plazas, numero_plazas, 0))
            rows_count = cur.rowcount
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return rows_count
    
    def showBus(self,nombre):
        sql = "select * from bus where nombre_bus = %s"
        try:
            cur.execute(sql, (nombre,))
            bus = cur.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        return bus

    def deleteBus(self,nombre):
        sql = "DELETE FROM bus WHERE nombre_bus = %s"
        try:
            cur.execute(sql, (nombre,))
            rows_deleted = cur.rowcount
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        return rows_deleted

    
    def showBuses(self):
        sql = "SELECT * FROM bus"
        try:
            cur.execute(sql)
            buses = cur.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        return buses



    def updatePlazasDisponibles(self,plazasDisponibles,nombre):
        sql = """UPDATE bus SET plazas_disponibles = (%s) WHERE nombre_bus = (%s)""" 
        try:
            cur.execute(sql,(plazasDisponibles, nombre))
            rows_set = cur.rowcount
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        return rows_set


    def updatePlazasVendidas(self,plazasVendidas,nombre):
        sql = """UPDATE bus SET plazas_vendidas = (%s) WHERE nombre_bus = (%s)""" 
        try:
            cur.execute(sql,(plazasVendidas, nombre))
            rows_set = cur.rowcount
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        return rows_set
    
