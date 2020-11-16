Algoritmo multiplos_De_2
	Escribir "Introducir hasta que numero quiere contar"
	Leer num
	x = 0
	cont = 0
	suma = 0
	Mientras x <= num Hacer
		Si x%2==0 Entonces
			Escribir x
			cont = cont + 1
			suma = suma + x	
		Fin Si
		x = x +1
	Fin Mientras
	Escribir "Contador: " cont
	Escribir "Suma: " suma
FinAlgoritmo
