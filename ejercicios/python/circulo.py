from Figura import Figura

from math import pi

class Circulo(Figura):
    def __init__(self, radio, coordenada):
        self.Setradio(radio)
        Figura.__init__(self,coordenada)


    def Setradio(self,radio):
        self.__radio = radio

    def Getradio(self):
        return self.__radio

    def calcularSuperficie(self):
        self.__superficie = pi*self.Getradio()**2
        return self.__superficie
