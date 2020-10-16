def multiplicar(num):
    for i in range(0,11):
        print(str(num)+" * "+str(i)+" = "+str(i*num))


numero = int(input("Introducir numero: "))
multiplicar(numero)