import psycopg2


class Bus:
    def __init__(self):
        pass
        

    def insertBus(self,conexion,nombre,numero_plazas ):
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