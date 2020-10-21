from Cordenada import Cordenada

from math import pi

class Circulo:
    def __init__(self, radio, cordenadaX, cordenadaY):
        self.Setradio(radio)
        self.cordenadaCirculo = Cordenada(cordenadaX, cordenadaY)


    def Setradio(self,radio):
        self.radio = radio

    def Getradio(self):
        return self.radio

    def calcularSuperficie(self):
        self.superficie = pi*self.Getradio()**2
        return self.superficie
