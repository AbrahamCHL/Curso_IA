from Bus import Bus 
from Pasajero import Pasajero


def accionesPasajero(pasajero, buses, posicionPasajero):
    opcion = 0
    while opcion != 4:
        print("Menu\n1-Comprar billetes\n2-Devolver billetes\n3-Estado del pasajero\n4-Sortir")
        try:
            opcion = int(input("Introducir una opción: "))
        except ValueError:
            print("Opción no valida")
        if opcion == 1:
            if not buses:
                print("No hay buses")
            else:
                print(f"Total de buses: {len(buses)}")
                for x in range(len(buses)):
                    print(buses[x].getNombre())
                
                nombreBus_encontrado = False
                nombreBus = input("Introduzca el nombre del bus donde quiere comprar: ")
                for x in range(len(buses)):
                    if nombreBus == buses[x].getNombre():
                        posicion = x
                        nombreBus_encontrado = True

                if nombreBus_encontrado == True:
            
                    demanda = int(input("Introduzca la cantidad de billetes que quiere comprar: "))
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

        elif opcion == 2:
            if not pasajero.getBilletesComprados():
                print("No ha hecho ninguna compra")
            else:
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
                  
        elif opcion == 3:
            print(f"El nombre del pasajero es: {pasajero.getNombre()}")
            print(f"Los apellidos del pasajeron son: {pasajero.getApellido()}")
            print(f"El DNI del pasajero es: {pasajero.getDni()}")
            print(f"La direccion donde quiere ir el pasajero es: {pasajero.getDireccion()}")
            if not pasajero.getBilletesComprados():
                print("No ha hecho ninguna compra")
            else:
                print(pasajero.getBilletesComprados())

        else:
            print("Introducir una opcion correcta")


def menuPasajero(pasajeros,buses):
    opcion = 0
    while opcion!=4:
        print("Menu Pasajero\n1-Crear pasajero\n2-Ingresar como pasajero\n3-Eliminar pasajero\n4-Salir")
        try:
            opcion = int(input("Introducir una opción: "))
        except ValueError:
            print("Opción no valida")
        if opcion==1:
            nombre = input("Introducir nombre: ")
            apellido = input("Introducir apellido: ")
            direccion = input("Introducir la direccion: ")
            dni = input("Introducir el dni: ")
            existe_dni = False
            for x in range(len(pasajeros)):
                if dni == pasajeros[x].getDni():
                    existe_dni = True
            if existe_dni == True:
                
                print("Este dni ya existe en nuestra lista de pasajeros")
            else:
                pasajeros.append(Pasajero(nombre,apellido,direccion,dni))
                    
            
            
        elif opcion==2:
            if not pasajeros:
                print("No hay pasajeros")
            else:
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
                    
        
        elif opcion==3:
            if not pasajeros:
                print("No hay pasajeros")
            else:
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
                    
        else:
            print("Opcion no valida, introduzca una opcion correcta")


def menuBus(buses):
    opcion = 0
    while opcion!=4:
        print("Menu Bus\n1-Crear un bus\n2-Información de un bus\n3-Eliminar un bus\n4-Salir")
        try:
            opcion = int(input("Introducir una opción: "))
        except ValueError:
            print("Opción no valida")
        if opcion == 1:
            nombre_existe = False
            nombre = input("Introducir nombre del bus: ")
            for x in range(len(buses)):
                if nombre == buses[x].getNombre():
                    nombre_existe = True
            
            if nombre_existe == False:
                numero_plazas = int(input("Introducir numeros de plazas: "))
                try:
                    buses.append(Bus(numero_plazas, nombre))
                except Exception as ex:
                    print("Ha ingresado un numero de plazas negativo, porfavor ingrese un numero positivo")
            else:
                print("Este nombre de bus ya existe ingrese otro")
            
                
        elif opcion == 2:
            if not buses:
                print("No hay buses")
            else:
                nombre_existe = False
                print(f"Hay: {len(buses)}")
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
                            print(f"EL dni del pasajero es: {buses[posicion].getPasajeros()[x].getDni()}")
                else:
                    print("Este nombre de bus no existe")
                
        elif opcion == 3:
            if not buses:
                print("No hay buses")
            else:
                nombre_existe = False
                print(f"Hay: {len(buses)}")
                nombreBus = input("Introducir nombre del bus que quiere borrar: ")
                for x in range(len(buses)):
                    if nombreBus == buses[x].getNombre():
                        posicion = x
                        nombre_existe = True

                if nombre_existe == True:
                    buses.pop(posicion)
                    print("Bus borrado correctamente")
                else:
                    print("Este nombre de bus no existe")
        else:
            print("Introducir una opción correcta")

