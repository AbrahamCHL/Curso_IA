import math

def calculadora(operacion, num1, num2):
    
    if operacion == 1:
        print("Resta")
        print(str(num1)+" - "+str(num2)+" = "+str(num1-num2))
    elif operacion == 2:
        print("Suma")
        print(str(num1)+" + "+str(num2)+" = "+str(num1+num2))
    elif operacion == 3:
        print("Multiplicación")
        print(str(num1)+" * "+str(num2)+" = "+str(num1*num2))
    elif operacion == 4:
        print("División")
        print(str(num1)+" / "+str(num2)+" = "+str(num1/num2))

opc = 0

while opc!=5:
    print("Calculadora")
    print("1-Resta")
    print("2-Suma")
    print("3-Multiplicacion")
    print("4-Division")
    print("5-Salir")
    opc = int(input("Elegir operación: "))
    if opc == 1 or opc == 2 or opc == 3 or opc == 4:
        numero1 = int(input("Introducir el primer numero: "))
        numero2 = int(input("Introducir el segundo numero: "))
        calculadora(opc,numero1,numero2)
    
   
