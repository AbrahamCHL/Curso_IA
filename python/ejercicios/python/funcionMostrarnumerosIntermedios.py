def mostrarNumeros(num1, num2):
    cadena = ""
    for i in range(num1,num2):
        if i != num1 and i!=num2:
            cadena +=str(i)+"\n"
    
    cadena = cadena[:-1]
    return cadena


numero1 = int(input("Introducir el primer numero: "))
numero2 = int(input("Introducir el segundo numero: "))

print(mostrarNumeros(numero1,numero2))