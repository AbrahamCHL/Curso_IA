import random

totalNum = int(input("Que tamaño quiere que tenga la lista: "))
numeroBuscar = int(input("Introducir numero a buscar: "))
encontrado = False
cont = 0
listaNumeros = [0] * totalNum
for x in range(totalNum):
    listaNumeros[x] = random.randint(0,10)


while encontrado == False and cont < len(listaNumeros):
    if numeroBuscar == listaNumeros[cont]:
        encontrado = True
        print("El numero fue encontrado")
    cont += 1

if encontrado == False:
    print("EL numero no fue encontrado")

print(listaNumeros)