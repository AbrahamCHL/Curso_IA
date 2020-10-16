def determinarMes(numero_mes):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo","Junio","Julio","Agosto","Septiembre", "Octubre", "Noviembre", "Diciembre"]
    encontrado = False
    for i in range(len(meses)):
        if i == numero_mes-1:
            print("El mes es: "+meses[numero_mes-1])
            encontrado = True
  
    if encontrado==False:
        print("El numero de mes es incorrecto")




numeroMes = int(input("Introducir numero del mes: "))
determinarMes(numeroMes)