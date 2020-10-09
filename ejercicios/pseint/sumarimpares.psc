Algoritmo sumar_impares_unidad
	suma = 0
	num = 100
	Mientras num > 0 Hacer
		Si num%2<>0 Entonces
			Escribir num
			suma = suma + num 
		Fin Si
		num = num - 1
		
	Fin Mientras
	Escribir "La suma de los impares es: " suma
FinAlgoritmo
