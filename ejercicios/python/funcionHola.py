def hola(num_repeticiones):
    cadena = "hola\n"*num_repeticiones
    cadena = cadena[:-1]

    return cadena

numero = int(input("Introducir el numero de repeticiones: "))
print(hola(numero))