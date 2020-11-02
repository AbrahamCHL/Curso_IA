import psycopg2
from Conexion import cur

class Pasajero:

    def __init__(self):
        pass

    def insertPasajero(self,dni,nombre,apellido,direccion):
        rows_count = 0
        sql = """INSERT INTO public.pasajero(
            dni, apellido, nombre, direccion)
            VALUES (%s, %s, %s, %s);"""
        try:
            cur.execute(sql, (dni,apellido, nombre, direccion))
            rows_count = cur.rowcount
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return rows_count
    

    def showPasajero(self,dni):
        sql = "select * from pasajero where dni = %s"
        try:
            cur.execute(sql, (dni,))
            pasajero = cur.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        return pasajero


    def showPasajeros(self):
        sql = "SELECT * FROM pasajero"
        try:
            cur.execute(sql)
            pasajeros = cur.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        return pasajeros

    def deletePasajero(self,dni):
        sql = "DELETE FROM pasajero WHERE dni = %s"
        try:
            cur.execute(sql, (dni,))
            rows_deleted = cur.rowcount
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        return rows_deleted
    
    