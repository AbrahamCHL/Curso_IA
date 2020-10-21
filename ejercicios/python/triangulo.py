from Cordenada import Cordenada


class Triangulo:
    def __init__(self, base, altura, cordenadaX, cordenadaY):
        self.Setbase(base)
        self.Setaltura(altura)
        self.cordenadaTriangulo = Cordenada(cordenadaX, cordenadaY)


    def Setbase(self,base):
        self.base = base

    def Setaltura(self,altura):
        self.altura = altura

    def Getbase(self):
        return self.base

    def Getaltura(self):
        return self.altura

    def calcularSuperficie(self):
        self.superficie = self.Getbase() * (self.Getaltura() / 2)
        return self.superficie