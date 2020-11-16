from funciones import *

contactos = []

opcion = 0

while opcion!=4:
    print("Menu\n1.- Añadir contacto\n2.- Buscar contacto\n3.- Eliminar contacto\n4.- Salir")
    while True:
        try:
            opcion = int(input("Introducir una opción: "))
            break
        except ValueError:
            print("La opción debe de ser un digito")
    if opcion == 1:
        addContacto(contactos)

    elif opcion == 2:
        buscarContacto(contactos)

    elif opcion == 3:
        eliminarContacto(contactos)
    elif opcion == 4:
        print("Good bye")
    else:
        print("Opción no valida")

