from Bus import Bus 

buses = []
opcion = 0
while opcion!=4:
    print("Menu\n1-Crear bus\n2-Información de un bus\n3-Eliminar un bus\n4-Salir")
    opcion = int(input("Introducir una opción: "))
    if opcion == 1:
        numero_plazas = int(input("Introducir numeros de plazas: "))
        if numero_plazas > 0:
            buses.append(Bus(numero_plazas))
        else:
            print("Introducir un numero de plazas correcto")
    elif opcion == 2: 
        if not buses:
            print("No hay buses")
        else:
            print("Hay: "+str(len(buses)))
            posicion = int(input("Introducir el numero del bus que quiere visualizar: "))
            if posicion < len(buses):
                opc = 0
                while opc != 4:
                    print("Menu\n1-Venda de billets\n2-Devolucio de billets\n3-Estat de la venda\n4-Sortir")
                    opc = int(input("Introduzca una opcion: "))
                    if opc == 1:
                        demanda = int(input("Introduzca la cantidad de billetes que quiere comprar: "))
                        
                        if buses[posicion].ventaDeBilletes(demanda) == True:
                            print("Venta correcta, hay disponibles: "+str(buses[posicion].getPlazasDisponibles()))
                        else:
                            print("Venta incorrecta, no disponemos de plazas suficientes, quedan: "+str(buses[posicion].getPlazasDisponibles()))

                    elif opc == 2:
                        devolucion_billetes = int(input("Introduzca la cantidad de billetes a devolver: "))
                        if buses[posicion].devolucion(devolucion_billetes) == False:
                            print("No puede devolver esa cantidad")
                        else:    
                            print("El número de plazas disponibles es: " + str(buses[posicion].getPlazasDisponibles()))
                
                    elif opc == 3:
                        print("El número de plazas disponibles es de: " + str(buses[posicion].getPlazasDisponibles()))
                        print("El número de plazas máximo es de: " + str(buses[posicion].getNumeroPlazas()))
                        print("El número de plazas vendidas es de: " + str(buses[posicion].billetesVendidos()))
                    else:
                        print("Introducir una opcion correcta")
            else:
                print("Esa posicion de bus no existe")
                
            
    elif opcion == 3:
        if not buses:
            print("No hay buses")
        else:
            print("Hay: "+str(len(buses)))
            posicion = int(input("Introducir el numero del bus que quiere eliminar: "))
            if posicion < len(buses):
                buses.pop(posicion)
                print("Bus eliminado correctamente")
            else:
                print("Esa posicion de bus no existe")
    else:
        print("Introducir una opción correcta")


    
    



