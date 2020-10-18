def multiplicar(num):
    cadena = ""
    for i in range(0,11):
        cadena += str(num)+" * "+str(i)+" = "+str(i*num)+"\n"

    cadena = cadena[:-1]

    return cadena

numero = int(input("Introducir numero: "))
print(multiplicar(numero))