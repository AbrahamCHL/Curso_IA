class Direccion:
    def __init__(self, _calle, _provincia, _cp):
        self.__setCalle(_calle)
        self.__setProvincia(_provincia)
        self.__setCp(_cp)

    # GETTERS
    def getCalle(self):
        return self.__calle
    
    def getProvincia(self):
        return self.__provincia

    def getCp(self):
        return self.__cp

    # SETTERS

    def __setCalle(self,calle):
        self.__calle = calle
    
    def __setProvincia(self,provincia):
        self.__provincia = provincia
    
    def __setCp(self,cp):
        self.__cp = cp

    def __str__(self):
        return (f"Calle: {self.getCalle()} Provincia: {self.getProvincia()} cp: {self.getCp()}")