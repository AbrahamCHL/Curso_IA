from funcionesBus import *
from funcionesPasajero import *
from Conexion import conexion


if conexion.comprobacionConexion() == True:
    conexion.createTableBus()
    conexion.createTablePasajero()
    conexion.createTableTransaccion()
    conexion.commit()
    opcion = 0
    while opcion!=3:
        print("Menu\n1-Menu Bus\n2-Menu Pasajero\n3-Salir")
        while True:
            try:
                opcion = int(input("Introducir una opción: "))
                break
            except ValueError:
                print("La opción debe de ser un digito")
        if opcion == 1:
        
            menuBus()

        elif opcion == 2:
            menuPasajero()
        
        elif opcion == 3:
            print("Adiós")
        else:
            print("Opcion no valida, introduzca una opcion correcta")
        
    conexion.closeConection()

else:
    print("No se ha podido conectar a la base de datos")







