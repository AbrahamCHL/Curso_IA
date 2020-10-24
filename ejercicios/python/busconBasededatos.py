from Postgres import Postgres

postgres = Postgres()

postgres.createTable('bus')

opcion = 0
while opcion!=5:
    print("Menu\n1-Crear bus\n2-Información de un bus\n3-Eliminar un bus\n4-Mostrar tabla de buses\n5-Salir")
    opcion = int(input("Introducir una opción: "))
    if opcion == 1:
        numero_plazas = int(input("Introducir numeros de plazas: "))
        if numero_plazas > 0:
            postgres.insert(numero_plazas)
        else:
            print("Introducir un numero de plazas correcto")
    elif opcion == 2: 
        idBusAvisualizar = int(input("Introducir el id del bus que quiere visualizar: "))
        numeroPlazas, plazasDisponibles, plazasVendidas = postgres.selectSoloUno(idBusAvisualizar)

        opc = 0
        while opc != 4:
            print("Menu\n1-Venda de billets\n2-Devolucio de billets\n3-Estat de la venda\n4-Sortir")
            opc = int(input("Introduzca una opcion: "))
            if opc == 1:
                demanda = int(input("Introduzca la cantidad de billetes que quiere comprar: "))
                if demanda > plazasDisponibles:
                    print(f"Venta incorrecta, no disponemos de plazas suficientes, quedan: {plazasDisponibles}")
                else:
                    plazasDisponibles -= demanda
                    print(f"Venta correcta, quedan: {plazasDisponibles}")
                    plazasVendidas = numeroPlazas - plazasDisponibles
                    postgres.update(plazasDisponibles,plazasVendidas,idBusAvisualizar)

            elif opc == 2:
                devolucion_billetes = int(input("Introduzca la cantidad de billetes a devolver: "))
                if numeroPlazas < (devolucion_billetes + plazasDisponibles):
                    print(f"Devolución incorrecta, el número de plazas disponibles es: {plazasDisponibles}")
                else:
                    plazasDisponibles += devolucion_billetes
                    plazasVendidas = numeroPlazas - plazasDisponibles
                    print(f"Devolución correcta, el número de plazas disponibles es: {plazasDisponibles}")
                    postgres.update(plazasDisponibles,plazasVendidas,idBusAvisualizar)
                
        
            elif opc == 3:
                print(f"El número de plazas disponibles es de: {plazasDisponibles}")
                print(f"El número de plazas máximo es de: {numeroPlazas}")
                print(f"El número de plazas vendidas es de: {plazasVendidas}")
            else:
                print("Introducir una opcion correcta")
                      
    elif opcion == 3:
        idAborrar = int(input("Introducir el id del bus que quiere borrar: ")) 
        postgres.delete(idAborrar)

    elif opcion == 4:
        print(postgres.selectTodo())
       
    else:
        print("Introducir una opción correcta")


postgres.closeConection()