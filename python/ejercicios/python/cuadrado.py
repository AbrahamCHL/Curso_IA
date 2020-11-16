from Figura import Figura

class Cuadrado(Figura):
    
    def __init__(self,base, coordenada):
        self.Setbase(base)
        Figura.__init__(self,coordenada)

    def Setbase(self,base):
        self.__base = base

    def Getbase(self):
        return self.__base

    def calcularSuperficie(self):
        self.__superficie = self.Getbase()**2
        return self.__superficie