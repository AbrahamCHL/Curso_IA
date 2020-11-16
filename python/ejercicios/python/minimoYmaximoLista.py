import random

max = 0
totalNum = int(input("Que tamaño quiere que tenga la lista: "))

listaNumeros = [0] * totalNum
for x in range(totalNum):
    listaNumeros[x] = random.randint(1,10)

min = listaNumeros[0]
for x in listaNumeros:
    
    if max < x:
        max = x
    if min > x:
        min = x

print(str(max))
print(str(min))



print(listaNumeros)
