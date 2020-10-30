from Bus import Bus


def menuBus(conexion):
    cur = conexion.getConexion()
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
            crearBus(cur)

        elif opcion == 2:
            estadoBus(cur)
                
        elif opcion == 3:
            eliminarBus(cur)
        elif opcion == 4:
            print("Ha salido del menu bus")
        else:
            print("Introducir una opción correcta")
        conexion.commit()



def crearBus(cur):
    nombre_existe = False
    nombre = input("Introducir nombre del bus: ")
    while True:
        try:
            numero_plazas = int(input("Introducir numeros de plazas: "))
            break
        except ValueError:
            print("El numero de plazas debe de ser un digito")
    bus = Bus()
    if bus.insertBus(cur,nombre,numero_plazas) != 0:
        print("Bus creado correctamente")
       
    else:
        print("Error, el bus no se ha creado correctamente")
        

def estadoBus(cur): 
    nombreBus = input("Introducir nombre del bus que quiere ver: ")
    bus=Bus()
    busAmostrar = bus.showBus(cur,nombreBus)
    if len(busAmostrar)==0:
        print("El bus que ha introducido no existe")
    else:
        for row in busAmostrar:
            print(f"Id: {row[0]}")
            print(f"Nombre Bus: {row[1]}")
            print(f"Numero plazas: {row[2]}")
            print(f"Plazas disponibles: {row[3]}")
            print(f"Plazas vendidas: {row[4]}") 
    

def eliminarBus(cur):
    nombreBus = input("Introducir nombre del bus que quiere ver: ")
    bus = Bus()
    if bus.deleteBus(cur,nombreBus) == 0:
        print("El bus que ha introducido no existe")
    else:
        print("Bus eliminado correctamente")






