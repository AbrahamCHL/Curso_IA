from Direccion import Direccion

class Contacto:
    def __init__(self,_nombre,_apellidos, _telefono, _calle, _provincia, _cp):
        self.__setNombre(_nombre)
        self.__setApellidos(_apellidos)
        self.__setTelefono(_telefono)
        self.__direccion = Direccion(_calle,_provincia,_cp)


    # GETTERS
    def getNombre(self):
        return self.__nombre
    
    def getApellidos(self):
        return self.__apellidos

    def getTelefono(self):
        return self.__telefono

    # SETTERS

    def __setNombre(self,nombre):
        self.__nombre = nombre
    
    def __setApellidos(self,apellidos):
        self.__apellidos = apellidos
    
    def __setTelefono(self,telefono):
        self.__telefono = telefono
    

    def __str__(self):
        return (f"Nombre: {self.getNombre()} Apellidos: {self.getApellidos()} Telefono: {self.getTelefono()} Direccion: {self.__direccion.__str__()}")