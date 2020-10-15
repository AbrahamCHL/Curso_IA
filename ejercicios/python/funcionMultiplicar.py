def multiplicar(num):
    for i in range(0,10):
        mult = i * num
        print(str(num)+" * "+str(i)+" = "+str(mult))


numero = int(input("Introducir numero: "))
multiplicar(numero)