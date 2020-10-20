from math import pi

class Circulo:
    def __init__(self, radio):
        self.Setradio(radio)

    def Setradio(self,radio):
        self.radio = radio

    def Getradio(self):
        return self.radio

    def calcularSuperficie(self):
        self.superficie = pi*self.Getradio()**2
        return self.superficie
