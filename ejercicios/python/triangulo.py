from Figura import Figura

class Triangulo(Figura):
    def __init__(self, base, altura, coordenada):
        self.Setbase(base)
        self.Setaltura(altura)
        Figura.__init__(self,coordenada)


    def Setbase(self,base):
        self.__base = base

    def Setaltura(self,altura):
        self.__altura = altura

    def Getbase(self):
        return self.__base

    def Getaltura(self):
        return self.__altura

    def calcularSuperficie(self):
        self.__superficie = self.Getbase() * (self.Getaltura() / 2)
        return self.__superficie