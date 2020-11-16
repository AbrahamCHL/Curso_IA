from Transaccion import Transaccion
from AdminBus import AdminBus
from AdminPasajero import AdminPasajero
from Conexion import conexion
from AdmindTransaccion import AdminTransaccion

adminTransaccion = AdminTransaccion()
adminbus = AdminBus()

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
    buses = adminbus.showBuses()
    if len(buses)>0:
        cont = 0
        for row in buses:
            cont += 1
            print(f"{cont}.- adminbus: {row[0]} Plazas disponibles: {row[2]}")

        nombreBus = input("Introducir nombre del bus donde quiere comprar los billetes: ")
        busAmostrar = adminbus.showBus(nombreBus)
        if len(busAmostrar)>0:
            while True:
                try:
                    cantidad_billetes = int(input("Introducir la cantidad de billetes que quiere comprar: "))
                    break
                except ValueError:
                    print("La cantidad debe de ser un digito")
            if cantidad_billetes > 0:
                plazasDisponibles = busAmostrar[0][2]
                plazasVendidas = busAmostrar[0][3]
                if cantidad_billetes <= plazasDisponibles:
                    plazasDisponibles -= cantidad_billetes
                    plazasVendidas+= cantidad_billetes
                    transaccion = Transaccion(dni,nombreBus,cantidad_billetes)
                    if len(adminTransaccion.comprobarTransaccion(transaccion)) > 0:
                        if adminbus.updatePlazasDisponibles(plazasDisponibles,nombreBus) > 0 and adminbus.updatePlazasVendidas(plazasVendidas,nombreBus) > 0 and adminTransaccion.updateTransaccion(transaccion) > 0:
                            print("actulizado")
                        else:
                            print("No se ha podido actualizar las plazas")
                    else:
                        if adminbus.updatePlazasDisponibles(plazasDisponibles,nombreBus) > 0 and adminbus.updatePlazasVendidas(plazasVendidas,nombreBus) > 0 and adminTransaccion.comprarBilletes(transaccion) > 0:
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
    listaTransacciones = adminTransaccion.showTransaccion(dni)
    if len(listaTransacciones) > 0:
        print("-------------TRANSACCIONES-------------")
        for row in listaTransacciones:
            print(f"adminbus: {row[0]}")
            print(f"Cantidad de tickets: {row[2]}")
            print(f"Fecha compra: {row[3]}")
            print("")
        nombreBus = input("Introducir nombre del bus al que quiere devolver los billetes: ")
        transaccion = Transaccion(dni,nombreBus,0)
        busAmostrar = adminbus.showBus(nombreBus)
        comprobarBus = adminTransaccion.comprobarTransaccion(transaccion)
        if len(busAmostrar)>0 and len(comprobarBus) >0:
            while True:
                try:
                    cantidad_billetes = int(input("Introducir la cantidad de billetes que quiere devolver: "))
                    break
                except ValueError:
                    print("La cantidad debe de ser un digito")
            if cantidad_billetes > 0:
                plazasCompradas = comprobarBus[0][2]
                plazasDisponibles = busAmostrar[0][2]
                plazasVendidas = busAmostrar[0][3]
                plazasDisponibles += cantidad_billetes
                plazasVendidas -= cantidad_billetes
                if plazasCompradas - cantidad_billetes == 0:
                    adminbus.updatePlazasDisponibles(plazasDisponibles,nombreBus)
                    adminbus.updatePlazasVendidas(plazasVendidas,nombreBus)
                    adminTransaccion.deleteTransaccion(transaccion)
                    
                else:        
                    if cantidad_billetes <= plazasCompradas:
                       
                        if adminbus.updatePlazasDisponibles(plazasDisponibles,nombreBus) > 0 and adminbus.updatePlazasVendidas(plazasVendidas,nombreBus) > 0 and adminTransaccion.devolverBilletes(transaccion,cantidad_billetes) > 0:
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
    
    listaTransacciones = adminTransaccion.showTransaccion(dni)
    if len(listaTransacciones) > 0:
        print("-------------TRANSACCIONES-------------")
        for row in listaTransacciones:
            print(f"adminbus: {row[0]}")
            print(f"Cantidad de tickets: {row[2]}")
            print(f"Fecha compra: {row[3]}")
            print("")
    else:
        print("No tiene ninguna transaccion")

