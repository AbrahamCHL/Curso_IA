Algoritmo aumentar_disminuir_numero
	Escribir "Introducir primer numero: "
	Leer numero1
	Escribir "Introducir segundo numero: "
	Leer numero2
	cont = 0
	menor_es_mayor = Falso

	Si numero1 > numero2 Entonces
		numero_mayor = numero1
		numero_menor = numero2
	sino si numero2 > numero1 Entonces
		numero_mayor = numero2
		numero_menor = numero1
	SiNo
		Escribir "Los dos numeros son iguales "
	fin si	
	fin si
	
	Si numero_mayor > numero_menor Entonces
		Mientras menor_es_mayor==Falso Hacer
			numero_mayor = numero_mayor - 2
			numero_menor = numero_menor + 5
			Si numero_menor> numero_mayor Entonces
				menor_es_mayor = Verdadero
			Fin Si
			Escribir numero_mayor
			Escribir numero_menor
			cont = cont +1
		Fin Mientras
	Fin Si
	

	
FinAlgoritmo
