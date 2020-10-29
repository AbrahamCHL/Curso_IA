import psycopg2


class Conexion:
    def __init__(self):
        try:
            self.__conn = psycopg2.connect(host="localhost", port = 5432, database="postgres", user="admin", password="admin")
            self.__cur = self.__conn.cursor()
            print("Se ha conectado a la base de datos correctamente")
        except psycopg2.Error as err:
            print(f"Something went wrong: {err}")
        
    def getConexion(self):
        return self.__cur
    
    def closeConection(self):
        self.__cur.close()
        self.__conn.close()
    
    def commit(self):
        self.__conn.commit()