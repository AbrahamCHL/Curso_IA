class Triangulo:
    def __init__(self, base, altura):
        self.Setbase(base)
        self.Setaltura(altura)

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