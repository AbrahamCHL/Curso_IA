import psycopg2

class Pasajero:

    def __init__(self):
        pass

    def insertPasajero(self, cursor,dni,nombre,apellido,direccion):
        rows_count = 0
        sql = """INSERT INTO public.pasajero(
            dni, apellido, nombre, direccion)
            VALUES (%s, %s, %s, %s);"""
        try:
            cursor.execute(sql, (dni,apellido, nombre, direccion))
            rows_count = cursor.rowcount
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return rows_count
    

    def showPasajero(self,cursor,dni):
        sql = "select * from pasajero where dni = %s"
        try:
            cursor.execute(sql, (dni,))
            pasajero = cursor.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        return pasajero


    def showPasajeros(self,cursor):
        sql = "SELECT * FROM pasajero"
        try:
            cursor.execute(sql)
            pasajeros = cursor.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        return pasajeros

    def deletePasajero(self,cursor, dni):
        sql = "DELETE FROM pasajero WHERE dni = %s"
        try:
            cursor.execute(sql, (dni,))
            rows_deleted = cursor.rowcount
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
        return rows_deleted
    
    