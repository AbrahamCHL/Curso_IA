from Conexion import Conexion
from Bus import Bus

conexion = Conexion()
bus = Bus()

bus.createTable()

conexion.commit()
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

# postgres.createTable(sql)

# postgres.commit()
# opcion = 0

# opcion = 0

# while opcion!=3:
#     print("Menu\n1-Menu Bus\n2-Menu Pasajero\n3-Salir")
#     while True:
#         try:
#             opcion = int(input("Introducir una opción: "))
#             break
#         except ValueError:
#             print("La opción debe de ser un digito")
#     if opcion == 1:
#         menuBus(buses)

#     elif opcion == 2:
#         # menuPasajero(pasajeros,buses)
#         pass
    
#     elif opcion == 3:
#         print("Adiós")
#     else:
#         print("Opcion no valida, introduzca una opcion correcta")


# while opcion!=5:
#     print("Menu\n1-Crear bus\n2-Información de un bus\n3-Eliminar un bus\n4-Mostrar tabla de buses\n5-Salir")
#     opcion = int(input("Introducir una opción: "))
#     if opcion == 1:
#         numero_plazas = int(input("Introducir numeros de plazas: "))
#         if numero_plazas > 0:
#             sql = """INSERT INTO public.bus(
#                 numero_plazas, plazas_disponibles, plazas_vendidas)
#                 VALUES (%s,%s,%s)"""

#             postgres.insert(sql, numero_plazas)
#         else:
#             print("Introducir un numero de plazas correcto")
#     elif opcion == 2: 
#         idBusAvisualizar = int(input("Introducir el id del bus que quiere visualizar: "))
#         sql ="""SELECT id, numero_plazas, plazas_disponibles, plazas_vendidas
# 	    FROM public.bus WHERE id = %s"""
        
#         if postgres.selectSoloUno(sql,idBusAvisualizar) == False:
#             print("Este bus no existe")
#         else:
#             numeroPlazas, plazasDisponibles, plazasVendidas = postgres.selectSoloUno(sql,idBusAvisualizar)
#             opc = 0
            
                      
#     elif opcion == 3:
#         idAborrar = int(input("Introducir el id del bus que quiere borrar: ")) 
#         sql ="""DELETE FROM public.bus WHERE id = %s"""
#         postgres.delete(sql,idAborrar)

#     elif opcion == 4:
#         sql ="""SELECT id, numero_plazas, plazas_disponibles, plazas_vendidas
# 	    FROM public.bus """
#         print(postgres.selectTodo(sql))
       
#     else:
#         print("Introducir una opción correcta")
    
#     postgres.commit()

# postgres.closeConection()






# while opc != 4:
#     print("Menu\n1-Venda de billets\n2-Devolucio de billets\n3-Estat de la venda\n4-Sortir")
#     opc = int(input("Introduzca una opcion: "))
#     if opc == 1:
#         demanda = int(input("Introduzca la cantidad de billetes que quiere comprar: "))
#         if demanda > plazasDisponibles:
#             print(f"Venta incorrecta, no disponemos de plazas suficientes, quedan: {plazasDisponibles}")
#         else:
#             plazasDisponibles -= demanda
#             print(f"Venta correcta, quedan: {plazasDisponibles}")
#             plazasVendidas = numeroPlazas - plazasDisponibles
#             sql = """UPDATE public.bus SET plazas_disponibles = (%s),
#                 plazas_vendidas = (%s) WHERE id = (%s)""" 
#             postgres.update(sql,plazasDisponibles,plazasVendidas,idBusAvisualizar)

#     elif opc == 2:
#         devolucion_billetes = int(input("Introduzca la cantidad de billetes a devolver: "))
#         if numeroPlazas < (devolucion_billetes + plazasDisponibles):
#             print(f"Devolución incorrecta, el número de plazas disponibles es: {plazasDisponibles}")
#         else:
#             plazasDisponibles += devolucion_billetes
#             plazasVendidas = numeroPlazas - plazasDisponibles
#             print(f"Devolución correcta, el número de plazas disponibles es: {plazasDisponibles}")
#             sql = """UPDATE public.bus SET plazas_disponibles = (%s),
#                 plazas_vendidas = (%s) WHERE id = (%s)""" 
#             postgres.update(sql,plazasDisponibles,plazasVendidas,idBusAvisualizar)
    

#     elif opc == 3:
#         print(f"El número de plazas disponibles es de: {plazasDisponibles}")
#         print(f"El número de plazas máximo es de: {numeroPlazas}")
#         print(f"El número de plazas vendidas es de: {plazasVendidas}")
#     else:
#         print("Introducir una opcion correcta")
    
#     postgres.commit()