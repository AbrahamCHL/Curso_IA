class Bus:
    def __init__(self,_nombre,_plazas):
        self.__setNombre(_nombre)
        self.__setPlazas(_plazas)


    def __setNombre(self,_nombre):
        self.__nombre = _nombre

    
    def __setPlazas(self,_plazas):
        if _plazas <0:
            raise Exception("Ha ingresado un numero de plazas negativo, porfavor ingrese un numero positivo")
        
        self.__plazas = _plazas
    

    def getNombre(self):
        return self.__nombre


    def getPlazas(self):
        return self.__plazas