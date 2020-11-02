from Transaccion import Transaccion
from Bus import Bus
from Pasajero import Pasajero
from Conexion import conexion

pasajero = Pasajero()
transaccion = Transaccion()
bus = Bus()

def accionesPasajero(dni,pasajeroAmostrar):
    
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
            compraBilletes(dni)

        elif opcion == 2:
            
            devolverBilletes(dni)
                  
        elif opcion == 3:
            estadoPasajero(pasajeroAmostrar,dni)

        elif opcion == 4:
            print(f"Adiós")
        else:
            print("Introducir una opcion correcta")
        
        conexion.commit()


def compraBilletes(dni):
    buses = bus.showBuses()
    if len(buses)>0:
        cont = 0
        for row in buses:
            cont += 1
            print(f"{cont}.- Bus: {row[1]} Plazas disponibles: {row[3]}")

        nombreBus = input("Introducir nombre del bus donde quiere comprar los billetes: ")
        busAmostrar = bus.showBus(nombreBus)
        if len(busAmostrar)>0:
            while True:
                try:
                    cantidad_billetes = int(input("Introducir la cantidad de billetes que quiere comprar: "))
                    break
                except ValueError:
                    print("La cantidad debe de ser un digito")
            if cantidad_billetes > 0:
                plazasDisponibles = busAmostrar[0][3]
                plazasVendidas = busAmostrar[0][4]
                if cantidad_billetes <= plazasDisponibles:
                    plazasDisponibles -= cantidad_billetes
                    plazasVendidas+= cantidad_billetes
                    nombre_bus = busAmostrar[0][1]
                    if len(transaccion.comprobarTransaccion(nombre_bus, dni)) > 0:
                        if bus.updatePlazasDisponibles(plazasDisponibles,nombreBus) > 0 and bus.updatePlazasVendidas(plazasVendidas,nombreBus) > 0 and transaccion.updateTransaccion(dni,nombre_bus,cantidad_billetes) > 0:
                            print("actulizado")
                        else:
                            print("No se ha podido actualizar las plazas")
                    else:
                        if bus.updatePlazasDisponibles(plazasDisponibles,nombreBus) > 0 and bus.updatePlazasVendidas(plazasVendidas,nombreBus) > 0 and transaccion.comprarBilletes(dni,nombre_bus,cantidad_billetes) > 0:
                            print("ingresado")
                        else:
                            print("No se ha podido ingresar")
                else:
                    print("La cantidad de billetes que quiere comprar es mayor a las plazas disponibles")
            else:
                print("Introduzca una cantidad de billetes valida")
                

        else:
            print("El bus que ha introducido no existe")
    else:
        print("No hay buses")


def devolverBilletes(dni):
    listaTransacciones = transaccion.showTransaccion(dni)
    if len(listaTransacciones) > 0:
        print("-------------TRANSACCIONES-------------")
        for row in listaTransacciones:
            print(f"nombre_bus: {row[1]}")
            print(f"dni_pasajero: {row[2]}")
            print(f"cantidad de tickets: {row[3]}")
            print("")
        nombreBus = input("Introducir nombre del bus al que quiere devolver los billetes: ")
        busAmostrar = bus.showBus(nombreBus)
        comprobarBus = transaccion.comprobarBusDelPasajero(nombreBus,dni)
        if len(busAmostrar)>0 and len(comprobarBus) >0:
            while True:
                try:
                    cantidad_billetes = int(input("Introducir la cantidad de billetes que quiere devolver: "))
                    break
                except ValueError:
                    print("La cantidad debe de ser un digito")
            if cantidad_billetes > 0:
                plazasCompradas = comprobarBus[0][3]
                plazasDisponibles = busAmostrar[0][3]
                plazasVendidas = busAmostrar[0][4]
                if cantidad_billetes <= plazasCompradas:
                    plazasDisponibles += cantidad_billetes
                    plazasVendidas -= cantidad_billetes
                    if bus.updatePlazasDisponibles(plazasDisponibles,nombreBus) > 0 and bus.updatePlazasVendidas(plazasVendidas,nombreBus) > 0 and transaccion.devolverBilletes(dni,nombreBus,cantidad_billetes) > 0:
                        print("actulizado")
                    else:
                        print("No se ha podido actualizar las plazas")
                else:
                    print("La cantidad de billetes que quiere devolver es mayor a sus tickets comprados")
            else:
                print("Introduzca una cantidad de billetes valida")

        else:
            print("Error, no ha hecho ninguna transaccion con el bus que ha introducido")

    else:
        print("No tiene ninguna transaccion")



def estadoPasajero(pasajeroAmostrar,dni):
    print("-------------DATOS PASAJERO-------------")
    for row in pasajeroAmostrar:
        print(f"DNI: {row[0]}")
        print(f"Apellido: {row[1]}")
        print(f"Nombre: {row[2]}")
        print(f"Direccion: {row[3]}")
    
    listaTransacciones = transaccion.showTransaccion(dni)
    if len(listaTransacciones) > 0:
        print("-------------TRANSACCIONES-------------")
        for row in listaTransacciones:
            print(f"nombre_bus: {row[1]}")
            print(f"dni_pasajero: {row[2]}")
            print(f"cantidad de tickets: {row[3]}")
            print("")
    else:
        print("No tiene ninguna transaccion")

