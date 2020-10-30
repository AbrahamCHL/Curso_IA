from funcionesBus import *
from Conexion import Conexion

conexion = Conexion()


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
        conexion.createTableBus()
        conexion.commit()
        menuBus(conexion)

    elif opcion == 2:
        # menuPasajero(pasajeros,buses)
        pass
    
    elif opcion == 3:
        print("Adiós")
    else:
        print("Opcion no valida, introduzca una opcion correcta")
    
    

conexion.closeConection()



# sql ="""CREATE TABLE IF NOT EXISTS pasajero(
#    dni VARCHAR(9),
#    id_bus INT,
#    apellido VARCHAR(50) NOT NULL,
#    nombre VARCHAR(50) NOT NULL,
#    direccion VARCHAR(100),
#    billetes INT,
#    PRIMARY KEY(dni),
#    CONSTRAINT fk_bus
#       FOREIGN KEY(id_bus) 
# 	    REFERENCES bus(id_bus)
# )"""



