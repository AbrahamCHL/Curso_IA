class Transaccion:
    def __init__(self,dni_pasajero,nombre_bus,billetesAcomprar):
        self.__setDniPasajero(dni_pasajero)
        self.__setNombreBus(nombre_bus)
        self.__setBilletesAcomprar(billetesAcomprar)
    

    def getDniPasajero(self):
        return self.__dni_pasajero


    def getNombreBus(self):
        return self.__nombre_bus


    def getBilletesAcomprar(self):
        return self.__billetesAcomprar

    def __setDniPasajero(self,_dni):
        self.__dni_pasajero = _dni


    def __setNombreBus(self, _nombre):
        self.__nombre_bus = _nombre
    

    def __setBilletesAcomprar(self, _billetes):
        self.__billetesAcomprar = _billetes

    

   
    

   
