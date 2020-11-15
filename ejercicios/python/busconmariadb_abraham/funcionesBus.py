from Bus import Bus
from AdminBus import AdminBus
from Conexion import conexion

adminbus = AdminBus()

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
    buscreado = False
    nombre = input("Introducir nombre del bus: ")
    while True:
        try:
            numero_plazas = int(input("Introducir numeros de plazas: "))
            break
        except ValueError:
            print("El numero de plazas debe de ser un digito")
    
    try:
        bus = Bus(nombre,numero_plazas)
        buscreado = True
        if buscreado==True:
            if adminbus.insertBus(bus) > 0:
                print("Bus creado correctamente")
            else:
                print("Error, el bus no se ha creado correctamente")
        else:
            print("Error, el bus no se ha creado")
        
    except Exception as ex:
        print(ex)
    
    
    

def estadoBus(): 
    buses = adminbus.showBuses()
    if len(buses)>0:
        cont = 0
        for row in buses:
            cont += 1
            print(f"{cont}.- Bus: {row[0]}")
        nombreBus = input("Introducir nombre del bus que quiere ver: ")
        busAmostrar = adminbus.showBus(nombreBus)
        if len(busAmostrar)>0:
            for row in busAmostrar:
                print(f"Nombre Bus: {row[0]}")
                print(f"Numero plazas: {row[1]}")
                print(f"Plazas disponibles: {row[2]}")
                print(f"Plazas vendidas: {row[3]}")
            pasajeros = adminbus.mostrarPasajeros(nombreBus)
            if len(pasajeros) > 0:
                print("------------------PASAJEROS------------------")
                for row in pasajeros:
                    print(f"DNI: {row[0]}")
                    print(f"Nombre: {row[1]}")
                    print(f"Apellido: {row[2]}")
                    print(f"Dirección: {row[3]}")
                    print(f"Billetes: {row[4]}")
                    print(f"Fecha compra: {row[5]}")
                    print("")
            else:
                print("No hay pasajeros")
                        
        else:
            print("El bus que ha introducido no existe")

    else:
        print("No hay buses")

    
    
def eliminarBus():
    buses = adminbus.showBuses()
    if len(buses)>0:
        cont = 0
        for row in buses:
            cont += 1
            print(f"{cont}.- Bus: {row[0]}")
        nombreBus = input("Introducir nombre del bus que quiere eliminar: ")
        transaccionBus = adminbus.comprobarTransaccionBus(nombreBus)
        if len(transaccionBus) > 0:
            if adminbus.deleteTransaccionBus(nombreBus) > 0 and adminbus.deleteBus(nombreBus) > 0:
                print("Bus eliminado correctamente")
            else:
                print("El bus que ha introducido no existe")
        else:
            if adminbus.deleteBus(nombreBus) > 0:
                print("Bus eliminado correctamente")
            else:
                print("El bus que ha introducido no existe")
            
    else:
        print("No hay buses")

    






