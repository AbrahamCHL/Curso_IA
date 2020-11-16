Algoritmo capital_para
	Escribir "Escribir el capital"
	Leer capital	
	acumulador = 0
	capitalfinal = 0
	
	Para x<-0 Hasta 11 Con Paso 1 Hacer
		acumulador = capital * 0.1667
		capitalfinal = capitalfinal + acumulador
		acumulador = 0
	Fin Para
	capitalfinal = capitalfinal + capital
	Escribir capitalfinal
FinAlgoritmo
