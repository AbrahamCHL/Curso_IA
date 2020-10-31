import psycopg2

class Bus:
    def __init__(self):
        pass
        

    def insertBus(self,conexion,nombre,numero_plazas ):
        if numero_plazas <0:
            raise Exception("Ha ingresado un numero de plazas negativo, porfavor ingrese un numero positivo")
        
        rows_count = 0
        sql = """INSERT INTO public.bus(
            nombre_bus, numero_plazas, plazas_disponibles, plazas_vendidas)
            VALUES (%s, %s, %s, %s);"""
        try:
            conexion.execute(sql, (nombre,numero_plazas, numero_plazas, 0))
            rows_count = conexion.rowcount
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return rows_count
    
    def showBus(self,conexion, nombre):
        sql = "select * from bus where nombre_bus = %s"
        try:
            conexion.execute(sql, (nombre,))
            bus = conexion.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        return bus

    def deleteBus(self,conexion, nombre):
        sql = "DELETE FROM bus WHERE nombre_bus = %s"
        try:
            conexion.execute(sql, (nombre,))
            rows_deleted = conexion.rowcount
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        return rows_deleted

    
    def showBuses(self,conexion):
        sql = "SELECT * FROM bus"
        try:
            conexion.execute(sql)
            buses = conexion.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        return buses
    