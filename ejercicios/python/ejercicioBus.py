def ventaDeBilletes(numeroPlazas, billetesAcomprar):
    total_plazas = numeroPlazas - billetesAcomprar
    return total_plazas

def devolucion(numeroPlazas, BilletesADevolver):
    total_plazas = numeroPlazas + BilletesADevolver
    return total_plazas


numero_plazas = int(input("Introducir numeros de plazas: "))
opcion = None
maximo = numero_plazas

while opcion != 0:
    print("Menu\n1-Venda de billets\n2-Devolucio de billets\n3-Estat de la venda\n0-Sortir")
    opcion = int(input("Introduzca una opcion: "))
    if opcion == 1:
        demanda = int(input("Introduzca la cantidad de billetes que quiere comprar: "))
        if demanda > numero_plazas:
            print("No disponemos de plazas suficientes")
        else:
            numero_plazas= ventaDeBilletes(numero_plazas,demanda)
            print("Hay disponibles: "+str(numero_plazas))
            

    elif opcion == 2:
        devolucion_billetes = int(input("Introduzca la cantidad de billetes a devolver: "))
        if maximo < (devolucion_billetes + numero_plazas):
            print("El número máximo de plazas es de " + str(maximo))
        else:
            numero_plazas = devolucion(numero_plazas, devolucion_billetes) 
            print("El número de plazas disponibles es: " + str(numero_plazas))
    
    elif opcion == 3:
        print("El número de plazas disponibles es de: " + str(numero_plazas))
        print("El número de plazas máximo es de: " + str(maximo))
        print("El número de plazas vendidas es de: " + str(maximo - numero_plazas))


