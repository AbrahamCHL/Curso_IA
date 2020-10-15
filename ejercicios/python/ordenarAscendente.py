import random

totalNum = int(input("Que tamaño quiere que tenga la lista: "))
aux = 0


listaNumeros = [0] * totalNum 
for x in range(totalNum):
    listaNumeros[x] = random.randint(0,10)

print("Lista antes de ordenar: "+str(listaNumeros))

total = len(listaNumeros)
for i in listaNumeros:
    for j in range(total-1):
        if listaNumeros[j] > listaNumeros[j+1]:
            aux = listaNumeros[j]
            listaNumeros[j] = listaNumeros[j+1]
            listaNumeros[j+1] = aux
    


print("Lista despues de ordenar: "+str(listaNumeros))
