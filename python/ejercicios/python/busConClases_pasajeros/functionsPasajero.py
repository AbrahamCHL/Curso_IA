from Pasajero import Pasajero

def compraBilletes(pasajero,buses):
    print(f"Total de buses: {len(buses)}")
    for x in range(len(buses)):
        print(f"Bus: {buses[x].getNombre()}")
    
    nombreBus_encontrado = False
    nombreBus = input("Introduzca el nombre del bus donde quiere comprar: ")
    for x in range(len(buses)):
        if nombreBus == buses[x].getNombre():
            posicion = x
            nombreBus_encontrado = True

    if nombreBus_encontrado == True:
        while True:
            try:
                demanda = int(input("Introduzca la cantidad de billetes que quiere comprar: "))
                break
            except ValueError:
                print("Error, la cantidad de billetes debe de ser un digito")
        
        if buses[posicion].ventaDeBilletes(demanda) == True:
            buses[posicion].insertPasajero(pasajero)
            if nombreBus in pasajero.getBilletesComprados():
                pasajero.sumarBilletes(nombreBus,demanda)
            else:
                pasajero.insertarBilletes(nombreBus, demanda)
            print(f"Venta correcta, hay disponibles: {buses[posicion].getPlazasDisponibles()}")
        else:
            print(f"Venta incorrecta, no disponemos de plazas suficientes, quedan: {buses[posicion].getPlazasDisponibles()}")
    else:
        print("Este nombre de bus no existe")

def devolverBilletes(pasajero,buses,posicionPasajero):
    print(pasajero.getBilletesComprados())
    nombreBus_encontrado = False
    nombreBus = input("Introduzca el nombre del bus donde quiere devolver los billetes: ")
    for x in range(len(buses)):
        if nombreBus == buses[x].getNombre():
            posicion = x
            nombreBus_encontrado = True

    if nombreBus_encontrado == True:
        if nombreBus in pasajero.getBilletesComprados():
            devolucion_billetes = int(input("Introduzca la cantidad de billetes a devolver: "))
            if buses[posicion].devolucion(devolucion_billetes) == True and devolucion_billetes <= pasajero.getUnaPosicionDelDicBilletes(nombreBus):
                pasajero.restarBilletes(nombreBus,devolucion_billetes)
                if pasajero.getUnaPosicionDelDicBilletes(nombreBus) == 0:
                    pasajero.eliminarPosicionBilletes(nombreBus)
                    buses[posicion].eliminarPasajero(posicionPasajero)
                    
                print(f"Devolución correcta, en el bus hay disponibles: {buses[posicion].getPlazasDisponibles()} plazas")
            else:
                print(f"Devolución incorrecta")
    else:
        print("En este bus no ha comprado ningun billete")

def estadoPasajero(pasajero):
    print(f"El nombre del pasajero es: {pasajero.getNombre()}")
    print(f"Los apellidos del pasajeron son: {pasajero.getApellido()}")
    print(f"El DNI del pasajero es: {pasajero.getDni()}")
    print(f"La direccion donde quiere ir el pasajero es: {pasajero.getDireccion()}")
    if not pasajero.getBilletesComprados():
        print("No ha hecho ninguna compra")
    else:
        print(pasajero.getBilletesComprados())


def accionesPasajero(pasajero, buses, posicionPasajero):
    opcion = 0
    while opcion != 4:
        print("Menu\n1-Comprar billetes\n2-Devolver billetes\n3-Estado del pasajero\n4-Sortir")
        while True:
            try:
                opcion = int(input("Introducir una opción: "))
                break
            except ValueError:
                print("Opción debe de ser un digito")

        if opcion == 1:
            if not buses:
                print("No hay buses")
            else:
                compraBilletes(pasajero,buses)

        elif opcion == 2:
            if not pasajero.getBilletesComprados():
                print("No ha hecho ninguna compra")
            else:
                devolverBilletes(pasajero,buses,posicionPasajero)
                  
        elif opcion == 3:
            estadoPasajero(pasajero)

        elif opcion == 4:
            print(f"Adiós {pasajero.getNombre()}")
        else:
            print("Introducir una opcion correcta")


def crearPasajero(pasajeros):
    existe_dni = False
    nombre = input("Introducir nombre: ")
    apellido = input("Introducir apellido: ")
    direccion = input("Introducir la direccion: ")
    dni = input("Introducir el dni: ")
    for x in range(len(pasajeros)):
        if dni == pasajeros[x].getDni():
            existe_dni = True
    if existe_dni == True:
        
        print("Este dni ya existe en nuestra lista de pasajeros")
    else:
        pasajeros.append(Pasajero(nombre,apellido,direccion,dni))

def ingresarComoPasajero(pasajeros,buses):
    dni_encontrado = False
    print(f"Hay: {len(pasajeros)}")
    dni = input("Introducir el dni del pasajero: ")
    for x in range(len(pasajeros)):
        if dni == pasajeros[x].getDni():
            posicion = x
            dni_encontrado = True

    if dni_encontrado == True:
        
        accionesPasajero(pasajeros[posicion],buses, posicion)
    else:
        print("Error, el dni no existe")

def eliminarPasajero(pasajeros):
    dni_encontrado = False
    print(f"Hay: {len(pasajeros)}")
    dni = input("Introducir el dni del pasajero que quiere borrar: ")
    for x in range(len(pasajeros)):
        if dni == pasajeros[x].getDni():
            posicion = x
            dni_encontrado = True

    if dni_encontrado == True:
        
        pasajeros.pop(posicion)
        print("Pasajero borrado correctamente")
    else:
        print("Error, el dni no existe")

def menuPasajero(pasajeros,buses):
    opcion = 0
    while opcion!=4:
        print("Menu Pasajero\n1-Crear pasajero\n2-Ingresar como pasajero\n3-Eliminar pasajero\n4-Salir")
        while True:
            try:
                opcion = int(input("Introducir una opción: "))
                break                
            except ValueError:
                print("La opcion debe de ser un digito")

        if opcion==1:
            crearPasajero(pasajeros)
            
        elif opcion==2:
            if not pasajeros:
                print("No hay pasajeros")
            else:
                ingresarComoPasajero(pasajeros,buses)
                    
        elif opcion==3:
            if not pasajeros:
                print("No hay pasajeros")
            else:
                eliminarPasajero(pasajeros)
                    
        elif opcion==4:
            print("Ha salido del menu pasajero")
        else:
            print("Opcion no valida, introduzca una opcion correcta")