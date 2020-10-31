from Bus import Bus

def menuBus(conexion):
    cur = conexion.getConexion()
    bus = Bus()
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
            crearBus(cur,bus)

        elif opcion == 2:
            estadoBus(cur,bus)
                
        elif opcion == 3:
            eliminarBus(cur,bus)
        elif opcion == 4:
            print("Ha salido del menu bus")
        else:
            print("Introducir una opción correcta")
        conexion.commit()



def crearBus(cur,bus):
    nombre_existe = False
    nombre = input("Introducir nombre del bus: ")
    while True:
        try:
            numero_plazas = int(input("Introducir numeros de plazas: "))
            break
        except ValueError:
            print("El numero de plazas debe de ser un digito")
    
    
    try:
        if bus.insertBus(cur,nombre,numero_plazas) > 0:
            print("Bus creado correctamente")
        
        else:
            print("Error, el bus no se ha creado correctamente")
    except Exception as ex:
        print(ex)

    
def estadoBus(cur,bus): 
    buses = bus.showBuses(cur)
    if len(buses)>0:
        cont = 0
        for row in buses:
            cont += 1
            print(f"{cont}.- Bus: {row[1]}")
        nombreBus = input("Introducir nombre del bus que quiere ver: ")
        busAmostrar = bus.showBus(cur,nombreBus)
        if len(busAmostrar)>0:
            for row in busAmostrar:
                print(f"Id: {row[0]}")
                print(f"Nombre Bus: {row[1]}")
                print(f"Numero plazas: {row[2]}")
                print(f"Plazas disponibles: {row[3]}")
                print(f"Plazas vendidas: {row[4]}") 
        else:
            print("El bus que ha introducido no existe")

    else:
        print("No hay buses")

    
    

def eliminarBus(cur,bus):
    buses = bus.showBuses(cur)
    if len(buses)>0:
        cont = 0
        for row in buses:
            cont += 1
            print(f"{cont}.- Bus: {row[1]}")
        nombreBus = input("Introducir nombre del bus que quiere eliminar: ")
        if bus.deleteBus(cur,nombreBus) > 0:
            print("Bus eliminado correctamente")
        else:
            print("El bus que ha introducido no existe")
            
    else:
        print("No hay buses")

    






