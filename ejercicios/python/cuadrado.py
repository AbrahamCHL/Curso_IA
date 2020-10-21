from Cordenada import Cordenada

class Cuadrado:
    
    def __init__(self,base, cordenada):
        self.Setbase(base)
        self.cordenadaCuadrado = cordenada


    def Setbase(self,base):
        self.base = base

    def Getbase(self):
        return self.base

    def calcularSuperficie(self):
        self.superficie = self.Getbase()**2
        return self.superficie