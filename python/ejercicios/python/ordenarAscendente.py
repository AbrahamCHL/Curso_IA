import random

totalNum = int(input("Que tamaño quiere que tenga la lista: "))


listaNumeros = [0] * totalNum 
for x in range(totalNum):
    listaNumeros[x] = random.randint(0,10)

aux = 0
# listaNumeros = [10,7,6,2,3,1,4,5,8,9]
print("Lista antes de ordenar: "+str(listaNumeros))

for i in listaNumeros:
    for j in range(len(listaNumeros)-1):
        if listaNumeros[j] > listaNumeros[j+1]:
            aux = listaNumeros[j]
            listaNumeros[j] = listaNumeros[j+1]
            listaNumeros[j+1] = aux
    


print("Lista despues de ordenar: "+str(listaNumeros))
