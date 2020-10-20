class Cuadrado:
    
    def __init__(self,base):
        self.Setbase(base)

    def Setbase(self,base):
        self.base = base

    def Getbase(self):
        return self.base

    def calcularSuperficie(self):
        self.superficie = self.Getbase()**2
        return self.superficie