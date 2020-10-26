from functionsBus import * 

buses = []
pasajeros = []
dniPasajeros = []
opcion = 0

while opcion!=3:
    print("Menu\n1-Menu Bus\n2-Menu Pasajero\n3-Salir")
    opcion = int(input("Introducir una opción: "))
    if opcion == 1:
        menuBus(buses)

    elif opcion == 2:
        menuPasajero(pasajeros,buses)
    
    else:
        print("Opcion no valida, introduzca una opcion correcta")

                


    
    



