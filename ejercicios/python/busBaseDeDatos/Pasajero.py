class Pasajero():

    def __init__(self,_nombre,_apellido,_direccion, _dni):
        self.__nombre = _nombre
        self.__apellido = _apellido
        self.__direccion = _direccion
        self.__dni = _dni

    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getDireccion(self):
        return self.__direccion
    
    def getDni(self):
        return self.__dni

    def getBilletesAcomprar(self):
        return self.__billetesAcomprar

    def comprarBilletes(self, _billetesAcomprar, plazasDisponibles):
        compra = False
        if plazasDisponibles >= _billetesAcomprar:
            self.__billetesAcomprar = _billetesAcomprar
            compra = True
        else:
            compra = False
        
        return compra
    
    def devolverBilletes