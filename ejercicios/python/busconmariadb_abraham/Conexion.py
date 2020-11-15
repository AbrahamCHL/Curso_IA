import mysql.connector

class Conexion:
    def __init__(self):
        try:
            self.__conn = mysql.connector.connect(host="localhost", port = 3306, database="proyectobus", user="root", password="password")
            self.__cur = self.__conn.cursor()
        except mysql.connector.Error as error:
            self.__cur = 0
            print(error)
    
    def getConexion(self):
        return self.__cur
    
    
    def createTableBus(self):
        sql ="""CREATE TABLE IF NOT EXISTS bus
            (
                nombre VARCHAR(50) ,
                numero_plazas INT NOT NULL,
                plazas_disponibles INT NOT NULL,
                plazas_vendidas INT NOT NULL,
                PRIMARY KEY(nombre)
            )"""
        try:
            self.__cur.execute(sql)
        except mysql.connector.Error as error:
            print(error)
    
    def createTablePasajero(self):
        sql ="""CREATE TABLE IF NOT EXISTS pasajero(
            dni VARCHAR(9),
            apellido VARCHAR(50) NOT NULL,
            nombre VARCHAR(50) NOT NULL,
            direccion VARCHAR(100),
            PRIMARY KEY(dni))"""
        try:
            self.__cur.execute(sql)
        except mysql.connector.Error as error:
            print(error)


    def createTableTransaccion(self):
        sql ="""CREATE TABLE IF NOT EXISTS transaccion(
            nombre_bus VARCHAR(50),
            dni_pasajero VARCHAR(9),
            cantidad_billetes INT NOT NULL,
            fecha_compra TIMESTAMP NOT NULL,
            CONSTRAINT transaccion_pkey PRIMARY KEY (nombre_bus, dni_pasajero),
            CONSTRAINT fk_bus
                FOREIGN KEY(nombre_bus) 
                    REFERENCES bus(nombre)
            ,CONSTRAINT fk_pasajero
                FOREIGN KEY(dni_pasajero) 
                    REFERENCES pasajero(dni))
            """
        try:
            self.__cur.execute(sql)
        except mysql.connector.Error as error:
            print(error)

    
    
    def closeConection(self):
        self.__cur.close()
        self.__conn.close()
    
    def commit(self):
        self.__conn.commit()


conexion = Conexion()
cur = conexion.getConexion()