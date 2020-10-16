def mostrarNumeros(num1, num2):
    for i in range(num1,num2):
        if i != num1 and i!=num2:
            print(i)


numero1 = int(input("Introducir el primer numero: "))
numero2 = int(input("Introducir el segundo numero: "))

mostrarNumeros(numero1,numero2)