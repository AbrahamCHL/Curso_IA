class Pasajero():

    def __init__(self,_nombre,_apellido,_direccion, _dni):
        self.__nombre = _nombre
        self.__apellido = _apellido
        self.__direccion = _direccion
        self.__dni = _dni
        self.__dic_billetesComprados = {}

    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getDireccion(self):
        return self.__direccion
    
    def getDni(self):
        return self.__dni

    def getBilletesComprados(self):
        return self.__dic_billetesComprados

    def getUnaPosicionDelDicBilletes(self,_posicion):
        return self.__dic_billetesComprados[_posicion]

    def sumarBilletes(self,_posicion, _billetes):
        self.__dic_billetesComprados[_posicion] += _billetes

    
    def restarBilletes(self, _posicion, _billetes):
       self.__dic_billetesComprados[_posicion] -= _billetes

    def insertarBilletes(self,_posicion,_billetes):
        self.__dic_billetesComprados[_posicion] = _billetes
        
    
        
    

