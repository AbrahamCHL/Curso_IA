class Pasajero():

    def __init__(self,_nombre,_apellido,_direccion, _dni):
        self.__nombre = _nombre
        self.__apellido = _apellido
        self.__direccion = _direccion
        self.__dni = _dni
        self.__billetesComprados = 0

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
    

    def comprarBilletes(self,_billetesComprados):
        self.__billetesComprados = _billetesComprados

    
    def devolverBillete(self,_billetesADevolver):
        self.__billetesComprados -= _billetesADevolver
        
    

