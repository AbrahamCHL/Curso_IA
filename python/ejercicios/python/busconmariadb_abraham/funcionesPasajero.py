from Pasajero import Pasajero
from accionesPasajero import accionesPasajero
from Conexion import conexion
from AdminPasajero import AdminPasajero
from AdminBus import AdminBus

adminbus = AdminBus()
adminpasajero = AdminPasajero()

def menuPasajero():
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
            crearPasajero()
            
        elif opcion==2:
            ingresarComoPasajero()
            pass
                    
        elif opcion==3:
            eliminarPasajero()
                    
        elif opcion==4:
            print("Ha salido del menu pasajero")
        else:
            print("Opcion no valida, introduzca una opcion correcta")
        
        conexion.commit()

def crearPasajero():
    dni = input("Introducir el dni: ")
    nombre = input("Introducir nombre: ")
    apellido = input("Introducir apellido: ")
    direccion = input("Introducir la direccion: ")

    pasajero = Pasajero(dni,nombre,apellido,direccion)
    
    if adminpasajero.insertPasajero(pasajero) > 0:
        print("Pasajero creado correctamente")
    else:
        print("Error, el pasajero no se ha creado")



def ingresarComoPasajero():
    pasajeros = adminpasajero.showPasajeros()
    if len(pasajeros)>0:
        cont =0
        for row in pasajeros:
            cont += 1
            print(f"{cont}.- DNI: {row[0]} Apellido: {row[1]} Nombre: {row[2]}")
        dniAbuscar = input("Introducir dni del pasajero: ")
        pasajeroAmostrar = adminpasajero.showPasajero(dniAbuscar)
        if len(pasajeroAmostrar)>0:
            accionesPasajero(dniAbuscar,pasajeroAmostrar)
        else:
            print("El pasajero que ha introducido no existe")
    else:
        print("No hay pasajeros")


def eliminarPasajero():
    pasajeros = adminpasajero.showPasajeros()
    if len(pasajeros)>0:
        cont =0
        for row in pasajeros:
            cont += 1
            print(f"{cont}.- DNI: {row[0]} Apellido: {row[1]} Nombre: {row[2]}")
            
        dniAborrar = input("Introducir dni del pasajero a borrar: ")
        
        transaccionPasajero = adminpasajero.comprobarTransaccionPasajero(dniAborrar)
        if len(transaccionPasajero):
            for row in transaccionPasajero:
                busAmostrar = adminbus.showBus(row[0])
                plazasCompradas = row[2]
                plazasDisponibles = busAmostrar[0][2]
                plazasVendidas = busAmostrar[0][3]
                plazasDisponibles += plazasCompradas
                plazasVendidas -= plazasCompradas
                if adminbus.updatePlazasDisponibles(plazasDisponibles,row[0]) > 0 and adminbus.updatePlazasVendidas(plazasVendidas,row[0]) > 0:
                    print("actulizado")
                else:
                    print("No se ha podido actualizar las plazas")
            if adminpasajero.deleteTransaccionPasajero(dniAborrar) > 0 and adminpasajero.deletePasajero(dniAborrar) > 0:
                print("Pasajero eliminado correctamente")
            else:
                print("El pasajero que ha introducido no existe")
        else:
            if adminpasajero.deletePasajero(dniAborrar) > 0:
                print("Pasajero eliminado correctamente")
            else:
                print("El pasajero que ha introducido no existe")                 
    else:
        print("No hay pasajeros")

