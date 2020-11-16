from Bus import Bus 


def crearBus(buses):
    nombre_existe = False
    nombre = input("Introducir nombre del bus: ")
    
    for x in range(len(buses)):
        if nombre == buses[x].getNombre():
            nombre_existe = True
    
    if nombre_existe == False:
        while True:
            try:
                numero_plazas = int(input("Introducir numeros de plazas: "))
                break
            except ValueError:
                print("El numero de plazas debe de ser un digito")
        try:
            buses.append(Bus(numero_plazas, nombre))
            print("Se ha creado el bus correctamente")
        except Exception as ex:
            print("Ha ingresado un numero de plazas negativo, porfavor ingrese un numero positivo")
    else:
        print("Este nombre de bus ya existe ingrese otro")

def estadoBus(buses):
    nombre_existe = False
    print(f"Total buses: {len(buses)}")
    for x in range(len(buses)):
        print(f"Bus: {buses[x].getNombre()}")
     
    nombreBus = input("Introducir nombre del bus que quiere ver: ")
               
    for x in range(len(buses)):
        if nombreBus == buses[x].getNombre():
            posicion = x
            nombre_existe = True
    if nombre_existe == True:
        
        print(f"El número de plazas disponibles es de: {buses[posicion].getPlazasDisponibles()}")
        print(f"El número de plazas máximo es de: {buses[posicion].getNumeroPlazas()}")
        print(f"El número de plazas vendidas es de:{buses[posicion].billetesVendidos()}")
        if not buses[posicion].getPasajeros():
            print("No ha habido ventas")
        else:
            print(f"El total de pasajeros es: {len(buses[posicion].getPasajeros())}")
            for x in range(len(buses[posicion].getPasajeros())):
                print(f"El pasajero con dni: {buses[posicion].getPasajeros()[x].getDni()} ha comprado: {buses[posicion].getPasajeros()[x].getUnaPosicionDelDicBilletes(buses[posicion].getNombre())}")
    else:
        print("Este nombre de bus no existe")

def eliminarBus(buses):
    nombre_existe = False
    print(f"Total buses: {len(buses)}")
    for x in range(len(buses)):
        print(f"Bus: {buses[x].getNombre()}")
    
    nombreBus = input("Introducir nombre del bus que quiere ver: ")
            
    for x in range(len(buses)):
        if nombreBus == buses[x].getNombre():
            posicion = x
            nombre_existe = True

    if nombre_existe == True:
        buses.pop(posicion)
        print("Bus borrado correctamente")
    else:
        print("Este nombre de bus no existe")

def menuBus(buses):
    opcion = 0
    while opcion!=4:
        print("Menu Bus\n1-Crear un bus\n2-Mostrar estado de un bus\n3-Eliminar un bus\n4-Salir")
        
        while True:
            try:
                opcion = int(input("Introducir una opción: "))
                break                
            except ValueError:
                print("La opcion debe de ser un digito")
        
        if opcion == 1:
            crearBus(buses)

        elif opcion == 2:
            if not buses:
                print("No hay buses")
            else:
                estadoBus(buses)
                
        elif opcion == 3:
            if not buses:
                print("No hay buses")
            else:
                eliminarBus(buses)
        elif opcion == 4:
            print("Ha salido del menu bus")
        else:
            print("Introducir una opción correcta")



