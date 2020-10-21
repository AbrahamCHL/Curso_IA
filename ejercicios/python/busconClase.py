from Bus import Bus 

numero_plazas = int(input("Introducir numeros de plazas: "))
if numero_plazas > 0:
    bus1 = Bus(numero_plazas)

    opcion = 6

    while opcion != 0:
        print("Menu\n1-Venda de billets\n2-Devolucio de billets\n3-Estat de la venda\n0-Sortir")
        opcion = int(input("Introduzca una opcion: "))
        if opcion == 1:
            demanda = int(input("Introduzca la cantidad de billetes que quiere comprar: "))
            
            if bus1.ventaDeBilletes(demanda) == True:
                print("Venta correcta, hay disponibles: "+str(bus1.getPlazasDisponibles()))
            else:
                print("Venta incorrecta, no disponemos de plazas suficientes, quedan: "+str(bus1.getPlazasDisponibles()))

        elif opcion == 2:
            devolucion_billetes = int(input("Introduzca la cantidad de billetes a devolver: "))
            if bus1.devolucion(devolucion_billetes) == False:
                print("No puede devolver esa cantidad")
            else:    
                print("El número de plazas disponibles es: " + str(bus1.getPlazasDisponibles()))
    
        elif opcion == 3:
            print("El número de plazas disponibles es de: " + str(bus1.getPlazasDisponibles()))
            print("El número de plazas máximo es de: " + str(bus1.getNumeroPlazas()))
            print("El número de plazas vendidas es de: " + str(bus1.billetesVendidos()))
        else:
            print("Introducir una opcion correcta")

else:
    print("Introducir un numero de plazas correcto")


