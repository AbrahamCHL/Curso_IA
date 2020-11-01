def accionesPasajero(cur,dni,pasajeroAmostrar):

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
           pass
            # compraBilletes(pasajero,buses)

        elif opcion == 2:
            pass
            # devolverBilletes(pasajero,buses,posicionPasajero)
                  
        elif opcion == 3:
            estadoPasajero(cur,dni,pasajeroAmostrar)

        elif opcion == 4:
            print(f"Adiós")
        else:
            print("Introducir una opcion correcta")


# def compraBilletes(pasajero,buses):
#     print(f"Total de buses: {len(buses)}")
#     for x in range(len(buses)):
#         print(f"Bus: {buses[x].getNombre()}")
    
#     nombreBus_encontrado = False
#     nombreBus = input("Introduzca el nombre del bus donde quiere comprar: ")
#     for x in range(len(buses)):
#         if nombreBus == buses[x].getNombre():
#             posicion = x
#             nombreBus_encontrado = True

#     if nombreBus_encontrado == True:
#         while True:
#             try:
#                 demanda = int(input("Introduzca la cantidad de billetes que quiere comprar: "))
#                 break
#             except ValueError:
#                 print("Error, la cantidad de billetes debe de ser un digito")
        
#         if buses[posicion].ventaDeBilletes(demanda) == True:
#             buses[posicion].insertPasajero(pasajero)
#             if nombreBus in pasajero.getBilletesComprados():
#                 pasajero.sumarBilletes(nombreBus,demanda)
#             else:
#                 pasajero.insertarBilletes(nombreBus, demanda)
#             print(f"Venta correcta, hay disponibles: {buses[posicion].getPlazasDisponibles()}")
#         else:
#             print(f"Venta incorrecta, no disponemos de plazas suficientes, quedan: {buses[posicion].getPlazasDisponibles()}")
#     else:
#         print("Este nombre de bus no existe")

# def devolverBilletes(pasajero,buses,posicionPasajero):
#     print(pasajero.getBilletesComprados())
#     nombreBus_encontrado = False
#     nombreBus = input("Introduzca el nombre del bus donde quiere devolver los billetes: ")
#     for x in range(len(buses)):
#         if nombreBus == buses[x].getNombre():
#             posicion = x
#             nombreBus_encontrado = True

#     if nombreBus_encontrado == True:
#         if nombreBus in pasajero.getBilletesComprados():
#             devolucion_billetes = int(input("Introduzca la cantidad de billetes a devolver: "))
#             if buses[posicion].devolucion(devolucion_billetes) == True and devolucion_billetes <= pasajero.getUnaPosicionDelDicBilletes(nombreBus):
#                 pasajero.restarBilletes(nombreBus,devolucion_billetes)
#                 if pasajero.getUnaPosicionDelDicBilletes(nombreBus) == 0:
#                     pasajero.eliminarPosicionBilletes(nombreBus)
#                     buses[posicion].eliminarPasajero(posicionPasajero)
                    
#                 print(f"Devolución correcta, en el bus hay disponibles: {buses[posicion].getPlazasDisponibles()} plazas")
#             else:
#                 print(f"Devolución incorrecta")
#     else:
#         print("En este bus no ha comprado ningun billete")


def estadoPasajero(cur,dni,pasajeroAmostrar):
    for row in pasajeroAmostrar:
        print(f"DNI: {row[0]}")
        print(f"Apellido: {row[1]}")
        print(f"Nombre: {row[2]}")
        print(f"Direccion: {row[3]}")

