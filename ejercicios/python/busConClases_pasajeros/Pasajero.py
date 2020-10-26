class Pasajero():

    def __init__(self,_nombre,_apellido,_direccion, _dni):
        self.__nombre = _nombre
        self.__apellido = _apellido
        self.__direccion = _direccion
        self.__dni = _dni
        self.__listaBuses = []

    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getDireccion(self):
        return self.__direccion
    
    def getDni(self):
        return self.__dni

    def getBilletesComprados(self):
        return self.__billetesComprados

    def comprarBilletes(self, _billetesAcomprar, plazasDisponibles,bus):
        compra = False
        if plazasDisponibles >= _billetesAcomprar:
            self.__billetesComprados = _billetesAcomprar
            
            compra = True
        else:
            compra = False
        self.__listaBuses.append(bus)
        return compra
    
    def devolverBillete(self,_billetesADevolver):

        if(_billetesADevolver <= self.getBilletesComprados()):
            self.__billetesComprados -= _billetesADevolver
    
    def getListaBuses(self):
        return self.__listaBuses

