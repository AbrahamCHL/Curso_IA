from Bus import Bus

numero_plazas = int(input("Introducir numeros de plazas: "))
bus1 = Bus(numero_plazas)

opcion = None

while opcion != 0:
    print("Menu\n1-Venda de billets\n2-Devolucio de billets\n3-Estat de la venda\n0-Sortir")
    opcion = int(input("Introduzca una opcion: "))
    if opcion == 1:
        demanda = int(input("Introduzca la cantidad de billetes que quiere comprar: "))
        if demanda > bus1.getPlazasDisponibles():
            print("No disponemos de plazas suficientes, quedan: "+str(bus1.getPlazasDisponibles()))
        else:
            bus1.ventaDeBilletes(demanda)
            print("Hay disponibles: "+str(bus1.getPlazasDisponibles()))
            
    elif opcion == 2:
        devolucion_billetes = int(input("Introduzca la cantidad de billetes a devolver: "))
        if bus1.getNumeroPlazas() < (devolucion_billetes + bus1.getPlazasDisponibles()):
            print("No puede devolver esa cantidad")
        else:
            bus1.devolucion(devolucion_billetes)
            print("El número de plazas disponibles es: " + str(bus1.getPlazasDisponibles()))
    
    elif opcion == 3:
        print("El número de plazas disponibles es de: " + str(bus1.getPlazasDisponibles()))
        print("El número de plazas máximo es de: " + str(bus1.getNumeroPlazas()))
        print("El número de plazas vendidas es de: " + str(bus1.billetesVendidos()))
    else:
        print("Introducir una opcion correcta")