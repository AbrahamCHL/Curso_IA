from circulo import Circulo
from triangulo import Triangulo
from cuadrado import Cuadrado
from Cordenada import Cordenada

opc = 0
while opc!=4:
    print("Menu\n1-Cuadrado\n2-Triángulo\n3-Círculo\n4-Salir")
    opc = int(input("De cual desea calcular su superficie: "))
    print("Introduzca las cordenadas donde lo quiere dibujar")
    cordenadaX = int(input("Introduzca cordenada X: "))
    cordenadaY = int(input("Introduzca cordenada Y: "))
    corde = Cordenada(cordenadaX,cordenadaY)

    if opc == 1:
        base = int(input("Introducir base del cuadrado: "))
        if base < 0:
            print("Entroduzca una base correcta")
        else:
            cuadrado1 = Cuadrado(base,corde)
            print("Cordenadas")
            print(cuadrado1.cordenadaCuadrado.GetX())
            print(cuadrado1.cordenadaCuadrado.GetY())

            print("La superficie es: "+str(cuadrado1.calcularSuperficie()))
        
    elif opc == 2:
        base = int(input("Introducir base del triangulo: "))
        altura = int(input("Introducir la altura del triangulo: "))
        if base < 0 or altura < 0:
            print("Error al introducir la base o la altura")
        else:
            triangulo1 = Triangulo(base,altura,cordenadaX, cordenadaY)
            print("Cordenadas")

            triangulo1.cordenadaTriangulo.GetX()
            triangulo1.cordenadaTriangulo.GetY()
            print("La superficie es: "+str(triangulo1.calcularSuperficie()))
    elif opc == 3:
        radio = int(input("Introducir el radio de un circulo: "))
        if radio < 0:
            print("Error al introducir el radio")
        else:
            circulo1 = Circulo(radio, cordenadaX, cordenadaY)
            print("Cordenadas")
            circulo1.cordenadaCirculo.GetX()
            circulo1.cordenadaCirculo.GetY()

            print("La superficie es: "+str(circulo1.calcularSuperficie()))

