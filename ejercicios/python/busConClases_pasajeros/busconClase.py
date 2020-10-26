from Bus import Bus 
from Pasajero import Pasajero

def crearPasajero(nombre, apellido, direccion, dni):
    pasajero = Pasajero(nombre,apellido,direccion,dni)
    
    return pasajero
def venderBillete(pasajero):
    billetes = int(input("Billetes a comprar: "))
    pasajero.comprarBilletes(billetes)
def menuPasajero(pasajero):
    opc = 0
    while opc != 4:
                    
                    print("Menu\n1-Venda de billets\n2-Devolucio de billets\n3-Estat de la venda\n4-Sortir")
                    opc = int(input("Introduzca una opcion: "))
                    if opc == 1:
                        print(f"Hay {len(buses)} buses")
                        posicion = int(input("Elige bus al que comprar billetes: "))                        
                        
                        
                        if posicion <= len(buses):
                            demanda = int(input("Introduzca la cantidad de billetes que quiere comprar: "))
                            if buses[posicion - 1].ventaDeBilletes(demanda) == True:
                                buses[posicion - 1].insertPasajero(pasajero)
                                print("Venta correcta, hay disponibles: "+str(buses[posicion - 1].getPlazasDisponibles()))
                            else:
                                print("Venta incorrecta, no disponemos de plazas suficientes, quedan: "+str(buses[posicion  -  1].getPlazasDisponibles()))
                        else:
                            print("Se ha introducido un bus inexistente.")
                    elif opc == 2:
                        print(pasajero.getListaBuses())
                        devolucion_billetes = int(input("Introduzca la cantidad de billetes a devolver: "))
                        pasajero.devolverBillete(devolucion_billetes)
                                      
                    elif opc == 3:
                        print("El número de plazas disponibles es de: " + str(buses[posicion  -  1].getPlazasDisponibles()))
                        print("El número de plazas máximo es de: " + str(buses[posicion  -  1].getNumeroPlazas()))
                        print("El número de plazas vendidas es de: " + str(buses[posicion  -  1].billetesVendidos()))
                    else:
                        print("Introducir una opcion correcta")
buses = []
pasajeros = []
dniPasajeros = []
opct = 0

while opct!=4 :
    print("Menu\n1-Bus\n2-Registro Pasajero\n3-Entrar Pasajero\n4-Salir")
    opct = int(input("Introducir una opción: "))
    if opct == 1:
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
                posicion = int(input("Introducir el numero del bus que quiere visualizar: "))
                if posicion <= len(buses):
                    print("El número de plazas disponibles es de: " + str(buses[posicion  -  1].getPlazasDisponibles()))
                    print("El número de plazas máximo es de: " + str(buses[posicion  -  1].getNumeroPlazas()))
                    print("El número de plazas vendidas es de: " + str(buses[posicion  -  1].billetesVendidos()))
                    print(f"El número de pasajeros que han comprado billetes a su nombre es: {buses[posicion - 1].getPasajeros()}")
                else:
                    print("Introducir una posicion correcta")
        elif opcion == 3:
            if not buses:
                print("No hay buses")
            else:
                print("Hay: "+str(len(buses)))
                posicion = int(input("Introducir el numero del bus que quiere eliminar: "))
                if posicion <= len(buses):
                    buses.pop(posicion - 1)
                    print("Bus eliminado correctamente")
                else:
                    print("Esa posicion de bus no existe")
        else:
            print("Introducir una opción correcta")
    
    elif opct == 2:
        nombre = input("Introducir nombre: ")
        apellido = input("Introducir apellido: ")
        direccion = input("Introducir la direccion: ")
        dni = input("Introducir el dni: ")
        pasajero = crearPasajero(nombre,apellido,direccion,dni)
        pasajeros.append(pasajero)
        dniPasajeros.append(pasajero.getDni())
        menuPasajero(pasajero)
        
    elif opct == 3:
        print(dniPasajeros)
        posicion = int(input("Introduce la posición de tu dni: "))
        if posicion <= len(dniPasajeros):
            menuPasajero(pasajeros[posicion - 1])

    pass

                


    
    



