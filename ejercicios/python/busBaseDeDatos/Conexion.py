import psycopg2

class Conexion:
    def __init__(self):
        self.__cur = 0
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
    
    def createTablePasajero(self):
        sql ="""CREATE TABLE IF NOT EXISTS pasajero(
            dni VARCHAR(9) UNIQUE,
            apellido VARCHAR(50) NOT NULL,
            nombre VARCHAR(50) NOT NULL,
            direccion VARCHAR(100),
            PRIMARY KEY(dni))"""
        try:
            self.__cur.execute(sql)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


    def createTableTransaccion(self):
        sql ="""CREATE TABLE IF NOT EXISTS transaccion(
            id_transaccion SERIAL,
            nombre_bus VARCHAR(50) NOT NULL,
            dni_pasajero VARCHAR(9) NOT NULL,
            cantidad_billetes INT NOT NULL,
            PRIMARY KEY(id_transaccion),
            CONSTRAINT fk_bus
                FOREIGN KEY(nombre_bus) 
                    REFERENCES bus(nombre_bus)
            ,CONSTRAINT fk_pasajero
                FOREIGN KEY(dni_pasajero) 
                    REFERENCES pasajero(dni))
            """
        try:
            self.__cur.execute(sql)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def getConexion(self):
        return self.__cur

    def comprobacionConexion(self):
        if self.__cur != 0:
            conexion = True
        else:
            conexion = False
        
        return conexion
        
    def closeConection(self):
        self.__cur.close()
        self.__conn.close()
    
    def commit(self):
        self.__conn.commit()


conexion = Conexion()
cur = conexion.getConexion()