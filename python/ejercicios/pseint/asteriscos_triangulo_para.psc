Algoritmo asteriscos_triangulo
	Escribir "Altura"
	Leer altura
	Para i<-1 Hasta altura Con Paso 1 Hacer
		Para j<-1 Hasta i Con Paso 1 Hacer
			Escribir "*" Sin Saltar
		Fin Para
		Escribir ""
	Fin Para
	
	Para x<-altura-1 Hasta 0 Con Paso -1 Hacer
		Para m<-1 Hasta x Con Paso 1 Hacer
			Escribir "*" Sin Saltar
		Fin Para
		Escribir ""
	Fin Para
	
FinAlgoritmo
