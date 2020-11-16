from Contacto import Contacto


def addContacto(listaContactos):
    nombre = input("Introducir nombre: ")
    apellidos = input("Introducir apellidos: ")
    telefono = input("Introducir telefono: ")
    calle = input("Introducir calle: ")
    provincia = input("Introducir provincia: ")
    cp = input("Introducir codigo postal: ")
    contacto = Contacto(nombre, apellidos, telefono, calle, provincia, cp)
    listaContactos.append(contacto)

def buscarContacto(listaContactos):
    contactoexiste = False
    if listaContactos:
        for x in listaContactos:
            print(x.getNombre())
        nombreBuscar = input("Introducir nombre del contacto a buscar: ")
        for x in range(len(listaContactos)):
            if nombreBuscar == listaContactos[x].getNombre():
                posicion = x
                contactoexiste = True
        
        if contactoexiste == True:
            print(listaContactos[posicion].__str__())
        else:
            print("El contacto no existe")
    else:
        print("No tiene contactos")

def eliminarContacto(listaContactos):
    contactoexiste = False
    if listaContactos:
        for x in listaContactos:
            print(x.getNombre())
        nombreBuscar = input("Introducir nombre del contacto a eliminar: ")
        for x in range(len(listaContactos)):
            if nombreBuscar == listaContactos[x].getNombre():
                posicion = x
                contactoexiste = True
        
        if contactoexiste == True:
            listaContactos.pop(posicion)
            print("Contacto eliminado")
        else:
            print("El contacto no existe")
    else:
        print("No tiene contactos")

