def determinarMes(numero_mes):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo","Junio","Julio","Agosto","Septiembre", "Octubre", "Noviembre", "Diciembre"]
    mes = ""
    mes = meses[numero_mes-1]
    return mes


numeroMes = int(input("Introducir numero del mes: "))
if numeroMes >= 1 and numeroMes <= 12:
    print(determinarMes(numeroMes))
else:
    print("Numero de mes incorrecto")
