Algoritmo calcular_horas_extras
	Escribir "Introduzca horas realizadas esta semana: "
	Leer horas
	salario = 400
	precio_hora = 10
	Si horas > 40 Y horas <= 48 Entonces
		horas_extras = horas - 40
		precio_hora = horas_extras * (precio_hora*2)
		salario = salario + precio_hora
	SiNo si horas > 48 Entonces
			horas_extras = horas - 48
			precio_hora = horas_extras * (precio_hora*3)
			salario = salario + precio_hora + 160
	Fin si		
	Fin Si
	Escribir salario

FinAlgoritmo
