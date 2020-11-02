from Bus import Bus
from Conexion import conexion
from Transaccion import Transaccion
from Pasajero import Pasajero

transaccion = Transaccion()
pasajero = Pasajero()
bus = Bus()

def menuBus():
    
    opcion = 0
    while opcion!=4:
        print("Menu Bus\n1-Crear un bus\n2-Mostrar estado de un bus\n3-Eliminar un bus\n4-Salir")
        
        while True:
            try:
                opcion = int(input("Introducir una opción: "))
                break                
            except ValueError:
                print("La opcion debe de ser un digito")
        
        if opcion == 1:
            crearBus()

        elif opcion == 2:
            estadoBus()
                
        elif opcion == 3:
            eliminarBus()
        elif opcion == 4:
            print("Ha salido del menu bus")
        else:
            print("Introducir una opción correcta")
        conexion.commit()


def crearBus():
    nombre_existe = False
    nombre = input("Introducir nombre del bus: ")
    while True:
        try:
            numero_plazas = int(input("Introducir numeros de plazas: "))
            break
        except ValueError:
            print("El numero de plazas debe de ser un digito")
    
    
    try:
        if bus.insertBus(nombre,numero_plazas) > 0:
            print("Bus creado correctamente")
        
        else:
            print("Error, el bus no se ha creado correctamente")
    except Exception as ex:
        print(ex)

    
def estadoBus(): 
    buses = bus.showBuses()
    if len(buses)>0:
        cont = 0
        for row in buses:
            cont += 1
            print(f"{cont}.- Bus: {row[1]}")
        nombreBus = input("Introducir nombre del bus que quiere ver: ")
        busAmostrar = bus.showBus(nombreBus)
        if len(busAmostrar)>0:
            print("-------------BUS-------------")
            for row in busAmostrar:
                print(f"Id: {row[0]}")
                print(f"Nombre Bus: {row[1]}")
                print(f"Numero plazas: {row[2]}")
                print(f"Plazas disponibles: {row[3]}")
                print(f"Plazas vendidas: {row[4]}")
            
            print("-------------PASAJEROS-------------")
            buscarPasajeros(nombreBus)

        else:
            print("El bus que ha introducido no existe")

    else:
        print("No hay buses")

    
    
def eliminarBus():
    buses = bus.showBuses()
    if len(buses)>0:
        cont = 0
        for row in buses:
            cont += 1
            print(f"{cont}.- Bus: {row[1]}")
        nombreBus = input("Introducir nombre del bus que quiere eliminar: ")
        if bus.deleteBus(nombreBus) > 0:
            print("Bus eliminado correctamente")
        else:
            print("El bus que ha introducido no existe")
            
    else:
        print("No hay buses")

    

def buscarPasajeros(nombre_bus):
    dni_pasajeros = transaccion.buscarPasajeros(nombre_bus)
    if len(dni_pasajeros):
        cont = 0
        dnis = []
        for row in dni_pasajeros:
            cont += 1
            dnis.append(row[0])
        for x in dnis:
            mostrarPasajero = pasajero.showPasajero(x)
            if len(mostrarPasajero) > 0:
                for row in mostrarPasajero:
                    print(f"DNI: {row[0]}")
                    print(f"Apellido: {row[1]}")
                    print(f"Nombre: {row[2]}")
                    print(f"Direccion: {row[3]}")
                    print("")
    else:
        print("No tiene pasajeros")
                


