import psycopg2

conn = psycopg2.connect(host="localhost", port = 5432, database="postgres", user="admin", password="admin")
cur = conn.cursor()

sql ="""CREATE TABLE IF NOT EXISTS public.bus 
(
    ID SERIAL PRIMARY KEY,
    NUMERO_PLAZAS integer NOT NULL,
    PLAZAS_DISPONIBLES integer,
    PLAZAS_VENDIDAS integer
)"""

cur.execute(sql)
conn.commit()

opcion = 0
while opcion!=5:
    print("Menu\n1-Crear bus\n2-Información de un bus\n3-Eliminar un bus\n4-Mostrar tabla de buses\n5-Salir")
    opcion = int(input("Introducir una opción: "))
    if opcion == 1:
        numero_plazas = int(input("Introducir numeros de plazas: "))
        if numero_plazas > 0:
            sql = """INSERT INTO public.bus(
                numero_plazas, plazas_disponibles, plazas_vendidas)
                VALUES (%s,%s,%s)"""
            cur.execute(sql, (numero_plazas,numero_plazas,0))
            conn.commit()
        else:
            print("Introducir un numero de plazas correcto")
    elif opcion == 2: 
        idBusAvisualizar = int(input("Introducir el id del bus que quiere visualizar: "))
        sql ="""SELECT id, numero_plazas, plazas_disponibles, plazas_vendidas
	    FROM public.bus WHERE id = %s"""
        cur.execute(sql,(idBusAvisualizar,))
        query_results = cur.fetchall()
        numeroPlazas = query_results[0][1]
        plazasDisponibles = query_results[0][2]
        plazasVendidas = query_results[0][3]
        
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
                    sql = """UPDATE public.bus SET plazas_disponibles = (%s),
                        plazas_vendidas = (%s) WHERE id = (%s)""" 
                    cur.execute(sql, (plazasDisponibles,plazasVendidas,idBusAvisualizar))
                    conn.commit()


            elif opc == 2:
                devolucion_billetes = int(input("Introduzca la cantidad de billetes a devolver: "))
                if numeroPlazas < (devolucion_billetes + plazasDisponibles):
                    print(f"Devolución incorrecta, el número de plazas disponibles es: {plazasDisponibles}")
                else:
                    plazasDisponibles += devolucion_billetes
                    plazasVendidas = numeroPlazas - plazasDisponibles
                    print(f"Devolución correcta, el número de plazas disponibles es: {plazasDisponibles}")
                    sql = """UPDATE public.bus SET plazas_disponibles = (%s),
                        plazas_vendidas = (%s) WHERE id = (%s)""" 
                    cur.execute(sql, (plazasDisponibles,plazasVendidas,idBusAvisualizar))
                    conn.commit()
                
        
            elif opc == 3:
                print(f"El número de plazas disponibles es de: {plazasDisponibles}")
                print(f"El número de plazas máximo es de: {numeroPlazas}")
                print(f"El número de plazas vendidas es de: {plazasVendidas}")
            else:
                print("Introducir una opcion correcta")
                      
    elif opcion == 3:
        idAborrar = int(input("Introducir el id del bus que quiere borrar: ")) 
        sql ="""DELETE FROM public.bus WHERE id = %s"""
        cur.execute(sql,(idAborrar,))
        conn.commit()
    elif opcion == 4:
        sql ="""SELECT id, numero_plazas, plazas_disponibles, plazas_vendidas
	    FROM public.bus """
        cur.execute(sql)
        query_results = cur.fetchall()
        print(query_results)
       
    else:
        print("Introducir una opción correcta")


cur.close()
conn.close()