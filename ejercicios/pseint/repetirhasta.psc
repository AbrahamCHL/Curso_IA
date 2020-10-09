Algoritmo repetir_hasta_numeros_pares
	suma = 0
	cont = 0
	media = 0
	Repetir
		Escribir "Introducir numero: "
		Leer num
		suma = suma + num
		cont = cont + 1
		

	Hasta Que num == 0
	
	
	Leer num 
	Mientras num <> 0 Hacer
		suma = suma + num
		cont = cont + 1
		Leer num
	Fin Mientras
	
	media = suma / cont
	Escribir "Suma: " suma
	Escribir  "Media: " media
FinAlgoritmo
