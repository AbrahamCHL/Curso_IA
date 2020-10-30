import psycopg2


class Conexion:
    def __init__(self):
        try:
            self.__conn = psycopg2.connect(host="localhost", port = 5432, database="postgres", user="admin", password="admin")
            self.__cur = self.__conn.cursor()
            print("Conexion a la base de datos correcta")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    
    def createTableBus(self):
        sql ="""CREATE TABLE IF NOT EXISTS bus
            (
                id_bus SERIAL,
                nombre_bus VARCHAR(50) UNIQUE,
                numero_plazas INT NOT NULL,
                plazas_disponibles INT,
                plazas_vendidas INT,
                PRIMARY KEY(id_bus)
            )"""
        try:
            self.__cur.execute(sql)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def getConexion(self):
        return self.__cur
    
    def closeConection(self):
        self.__cur.close()
        self.__conn.close()
    
    def commit(self):
        self.__conn.commit()