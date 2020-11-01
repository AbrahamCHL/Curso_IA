from Pasajero import Pasajero
from accionesPasajero import *

def menuPasajero(conexion):
    cur = conexion.getConexion()
    pasajero = Pasajero()
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
            crearPasajero(cur,pasajero)
            
        elif opcion==2:
            ingresarComoPasajero(conexion,cur,pasajero)
                    
        elif opcion==3:
            eliminarPasajero(cur,pasajero)
                    
        elif opcion==4:
            print("Ha salido del menu pasajero")
        else:
            print("Opcion no valida, introduzca una opcion correcta")
        
        conexion.commit()

def crearPasajero(cur,pasajero):
    dni = input("Introducir el dni: ")
    nombre = input("Introducir nombre: ")
    apellido = input("Introducir apellido: ")
    direccion = input("Introducir la direccion: ")
    
    if pasajero.insertPasajero(cur,dni,nombre,apellido,direccion) > 0:
        print("Pasajero creado correctamente")
    else:
        print("Error, el pasajero no se ha creado")



def ingresarComoPasajero(conexion,cur,pasajero):
    pasajeros = pasajero.showPasajeros(cur)
    if len(pasajeros)>0:
        cont =0
        for row in pasajeros:
            cont += 1
            print(f"{cont}.- DNI: {row[0]} Apellido: {row[1]} Nombre: {row[2]}")
        dniAbuscar = input("Introducir dni del pasajero: ")
        pasajeroAmostrar = pasajero.showPasajero(cur,dniAbuscar)
        if len(pasajeroAmostrar)>0:
            accionesPasajero(conexion,cur,dniAbuscar,pasajeroAmostrar)
        else:
            print("El pasajero que ha introducido no existe")
    else:
        print("No hay pasajeros")


def eliminarPasajero(cur,pasajero):
    pasajeros = pasajero.showPasajeros(cur)
    if len(pasajeros)>0:
        cont =0
        for row in pasajeros:
            cont += 1
            print(f"{cont}.- DNI: {row[0]} Apellido: {row[1]} Nombre: {row[2]}")
            
        dniAborrar = input("Introducir dni del pasajero a borrar: ")
        if pasajero.deletePasajero(cur,dniAborrar) > 0:
            print("Pasajero eliminado correctamente")
        else:
            print("El pasajero que ha introducido no existe")
    else:
        print("No hay pasajeros")

