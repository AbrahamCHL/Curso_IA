from Conexion import Conexion
import psycopg2


class Bus():
    def __init__(self,numeroPlazas, nombre):
        self.__nombreBus = nombre
        self.__numeroplazas = numeroPlazas
        self.__plazas_disponibles = numeroPlazas
        self.__lista_pasajeros = []
        self.__conexion = Conexion()

    def createTable(self):
        sql ="""CREATE TABLE IF NOT EXISTS bus
            (
                id_bus INT,
                numero_plazas INT NOT NULL,
                plazas_disponibles INT,
                plazas_vendidas INT,
                PRIMARY KEY(id_bus)
            )"""
        try:
            self.__conexion.getConexion().execute(sql)
        except psycopg2.Error as err:
            print(f"Something went wrong: {err}")
    
    # def getNombre(self):
    #     return self.__nombreBus

    # def getNumeroPlazas(self):
    #     return self.__numeroplazas

    # def getPlazasDisponibles(self):
    #     return self.__plazas_disponibles
    
    # def ventaDeBilletes(self,billetesAcomprar):
    #     ventacorrecta = False
    #     if billetesAcomprar > self.getPlazasDisponibles():
    #         #ventacorrecta = False
    #         pass
        
    #     else:
    #         self.__plazas_disponibles -= billetesAcomprar
    #         ventacorrecta = True

    #     return ventacorrecta

    # def insertPasajero(self,_pasajero):
    #     self.__lista_pasajeros.append(_pasajero)

    # def eliminarPasajero(self,_posicion):
    #     self.__lista_pasajeros.pop(_posicion)

    # def devolucion(self,BilletesADevolver):
    #     devolucioncorrecta = False
    #     if self.getNumeroPlazas() < (BilletesADevolver + self.getPlazasDisponibles()):
    #         #devolucioncorrecta = False
    #         pass
        
    #     else:
    #         self.__plazas_disponibles += BilletesADevolver
    #         devolucioncorrecta = True
    #     return devolucioncorrecta
    
    # def billetesVendidos(self):
    #     return self.getNumeroPlazas() - self.getPlazasDisponibles()

    # def getPasajeros(self):
    #     return self.__lista_pasajeros