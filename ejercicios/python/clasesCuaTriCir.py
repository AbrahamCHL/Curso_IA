from circulo import Circulo
from triangulo import Triangulo
from cuadrado import Cuadrado
from Coordenada import Coordenada

opc = 0
while opc!=4:
    print("Menu\n1-Cuadrado\n2-Triángulo\n3-Círculo\n4-Salir")
    opc = int(input("De cual desea calcular su superficie: "))
    print("Introduzca las cordenadas donde lo quiere dibujar")
    coordenadaX = int(input("Introduzca coordenada X: "))
    coordenadaY = int(input("Introduzca coordenada Y: "))
    coorde = Coordenada(coordenadaX,coordenadaY)

    if opc == 1:
        base = int(input("Introducir base del cuadrado: "))
        if base < 0:
            print("Entroduzca una base correcta")
        else:
            cuadrado1 = Cuadrado(base,coorde)
            print("Cordenadas")
            # cuadrado1.coordenadaCuadrado.x = 10
            # cuadrado1.coordenadaCuadrado.y = 50
            print(cuadrado1.coordenada.GetX())
            print(cuadrado1.coordenada.GetY())
            
            print("La superficie es: "+str(cuadrado1.calcularSuperficie()))
        
    elif opc == 2:
        base = int(input("Introducir base del triangulo: "))
        altura = int(input("Introducir la altura del triangulo: "))
        if base < 0 or altura < 0:
            print("Error al introducir la base o la altura")
        else:
            triangulo1 = Triangulo(base,altura,coorde)
            print("Cordenadas")

            print(triangulo1.coordenada.GetX())
            print(triangulo1.coordenada.GetY())
            print("La superficie es: "+str(triangulo1.calcularSuperficie()))
    elif opc == 3:
        radio = int(input("Introducir el radio de un circulo: "))
        if radio < 0:
            print("Error al introducir el radio")
        else:
            circulo1 = Circulo(radio, coorde)
            print("Cordenadas")
            print(circulo1.coordenada.GetX())
            print(circulo1.coordenada.GetY())

            print("La superficie es: "+str(circulo1.calcularSuperficie()))

