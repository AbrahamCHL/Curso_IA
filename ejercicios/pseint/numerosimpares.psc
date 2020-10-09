Algoritmo numeros_impares
	cont = 0
	num = 0
	Mientras num <= 100 Hacer
		Si num%2<>0 Entonces
			Escribir num
			cont = cont +1
		Fin Si
		num = num + 1
	Fin Mientras
	Escribir "El numero total de impares es: " cont
	
FinAlgoritmo
