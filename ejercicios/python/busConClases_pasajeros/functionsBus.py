from Bus import Bus 
from Pasajero import Pasajero


def accionesPasajero(pasajero, buses):
    opcion = 0
    while opcion != 4:
        print("Menu\n1-Comprar billetes\n2-Devolver billetes\n3-Estado del pasajero\n4-Sortir")
        try:
            opcion = int(input("Introducir una opción: "))
        except ValueError:
            print("Opción no valida")
        if opcion == 1:
            print(f"Hay {len(buses)} buses")
            posicion = int(input("Elige bus al que comprar billetes: "))                        
            
            if posicion <= len(buses) and posicion >0:
                demanda = int(input("Introduzca la cantidad de billetes que quiere comprar: "))
                if buses[posicion - 1].ventaDeBilletes(demanda) == True:
                    # buses[posicion - 1].insertPasajero(pasajero)
                    if posicion in pasajero.getBilletesComprados():
                        pasajero.sumarBilletes(posicion,demanda)
                    else:
                        pasajero.insertarBilletes(posicion, demanda)
                    print(f"Venta correcta, hay disponibles: {buses[posicion - 1].getPlazasDisponibles()}")
                else:
                    print(f"Venta incorrecta, no disponemos de plazas suficientes, quedan: {buses[posicion  -  1].getPlazasDisponibles()}")
            else:
                print("Se ha introducido un bus inexistente.")

        elif opcion == 2:
            if not pasajero.getBilletesComprados():
                print("No ha hecho ninguna compra")
            else:
                print(pasajero.getBilletesComprados())
                posicion = int(input("Elige bus al que quiere devolver los billetes: "))
                if posicion <= len(buses) and posicion >0:
                    if posicion in pasajero.getBilletesComprados():
                        devolucion_billetes = int(input("Introduzca la cantidad de billetes a devolver: "))
                        if buses[posicion - 1].devolucion(devolucion_billetes) == True and devolucion_billetes <= pasajero.getUnaPosicionDelDicBilletes(posicion):
                            pasajero.restarBilletes(posicion,devolucion_billetes)
                            if pasajero.getUnaPosicionDelDicBilletes(posicion) == 0:
                                pasajero.eliminarPosicionBilletes(posicion)
                                
                            print(f"Devolución correcta, en el bus hay disponibles: {buses[posicion - 1].getPlazasDisponibles()} plazas")
                        else:
                            print(f"Devolución incorrecta")
                    else:
                        print("En este bus no ha comprado ningun billete")
                else:
                    print("Se ha introducido un bus inexistente.")
                            
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
            pasajeros.append(Pasajero(nombre,apellido,direccion,dni))
            
        elif opcion==2:
            if not pasajeros:
                print("No hay pasajeros")
            else:
                print(f"Hay: {len(pasajeros)}")
                posicion = int(input("Introducir el numero del pasajero que quiere visualizar: "))
                if posicion <= len(pasajeros) and posicion>0:
                    if not buses:
                        print("No hay ningun bus")
                    else:
                        accionesPasajero(pasajeros[posicion-1],buses)
                else:
                    print("Esa posicion de pasajero no existe")

        elif opcion==3:
            if not pasajeros:
                print("No hay pasajeros")
            else:
                print(f"Hay: {len(pasajeros)}")
                posicion = int(input("Introducir el numero del pasajero que quiere eliminar: "))
                if posicion <= len(pasajeros) and posicion>0:
                    pasajeros.pop(posicion - 1)
                    print("Pasajero eliminado correctamente")
                else:
                    print("Esa posicion de pasajero no existe")
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
            numero_plazas = int(input("Introducir numeros de plazas: "))
            # if numero_plazas > 0:
            try:
                buses.append(Bus(numero_plazas))
            except Exception as ex:
                print("Ha ingresado un numero de plazas negativo, porfavor ingrese un numero positivo")
                
            # else:
                # print("Introducir un numero de plazas correcto")
        elif opcion == 2:
            if not buses:
                print("No hay buses")
            else:
                print(f"Hay: {len(buses)}")
                posicion = int(input("Introducir el numero del bus que quiere visualizar: "))
                if posicion <= len(buses) and posicion>0:
                    print(f"El número de plazas disponibles es de: {buses[posicion  -  1].getPlazasDisponibles()}")
                    print(f"El número de plazas máximo es de: {buses[posicion  -  1].getNumeroPlazas()}")
                    print(f"El número de plazas vendidas es de:{buses[posicion  -  1].billetesVendidos()}")
                    # print(f"El número de pasajeros que han comprado billetes a su nombre es: {buses[posicion - 1].getPasajeros()}")
                else:
                    print("Introducir una posicion correcta")
        elif opcion == 3:
            if not buses:
                print("No hay buses")
            else:
                print(f"Hay: {len(buses)}")
                posicion = int(input("Introducir el numero del bus que quiere eliminar: "))
                if posicion <= len(buses) and posicion>0:
                    buses.pop(posicion - 1)
                    print("Bus eliminado correctamente")
                else:
                    print("Esa posicion de bus no existe")
        else:
            print("Introducir una opción correcta")

