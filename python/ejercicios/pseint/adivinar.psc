Algoritmo Adivinar
	Escribir "Introducir numero para adivinar"
	Leer num
	
	
	Repetir
		Escribir "Cual crees que es el numero"
		Leer jugador
		Si num < jugador Entonces
			Escribir "Massa alt"
		SiNo si num > jugador Entonces
				Escribir "Massa baix"
			Fin si	
		Fin Si
	Hasta Que num==jugador
	Escribir "Lo has adivinado: " num
FinAlgoritmo
