from math import pi

class Cuadrado:
    
    def __init__(self, base):
        self.base = base

    def calcularSuperficie(self):
        self.superficie = self.base * self.base
        return self.superficie

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularSuperficie(self):
        self.superficie = self.base * (self.altura / 2)
        return self.superficie

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcularSuperficie(self):
        self.superficie = pi*self.radio**2
        return self.superficie

opc = 0
while opc!=4:
    print("Menu\n1-Cuadrado\n2-Triángulo\n3-Círculo\n4-Salir")
    opc = int(input("De cual desea calcular su superficie: "))
    if opc == 1:
        base = int(input("Introducir base del cuadrado: "))
        cuadrado1 = Cuadrado(base)
        print("La superficie es: "+str(cuadrado1.calcularSuperficie()))
    elif opc == 2:
        base = int(input("Introducir base del triangulo: "))
        altura = int(input("Introducir la altura del triangulo: "))
        triangulo1 = Triangulo(base,altura)
        print("La superficie es: "+str(triangulo1.calcularSuperficie()))
    elif opc == 3:
        radio = int(input("Introducir el radio de un circulo: "))
        circulo1 = Circulo(radio)
        print("La superficie es: "+str(circulo1.calcularSuperficie()))

