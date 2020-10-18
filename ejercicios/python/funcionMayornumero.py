def buscarNumeroMayor(lista_numeros):
    mayor = numeros[0]
    for i in lista_numeros:
        if i > mayor:
            mayor = i
    
    return mayor

numeros = [0] * 3

for i in range(3):
    numero = int(input("Introduce el número #{}: ".format(i + 1)))
    numeros[i] = numero

print("El numero mayor es: "+str(buscarNumeroMayor(numeros)))
