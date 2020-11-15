class Pasajero:

    def __init__(self,_dni,_nombre,_apellido,_direccion):
        self.__setDni(_dni)
        self.__setNombre(_nombre)
        self.__setApellido(_apellido)
        self.__setDireccion(_direccion)

    def getDni(self):
        return self.__dni

    
    def getNombre(self):
        return self.__nombre

    
    def getApellido(self):
        return self.__apellido

    def getDireccion(self):
        return self.__direccion


    def __setDni(self,dni):
        self.__dni = dni

    
    def __setNombre(self,nombre):
        self.__nombre = nombre

    
    def __setApellido(self,apellido):
        self.__apellido = apellido

    def __setDireccion(self,direccion):
        self.__direccion = direccion
        
    
    