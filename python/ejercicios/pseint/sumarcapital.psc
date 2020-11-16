Algoritmo buscar_capital
	Escribir "Introducir capital"
	Leer capital
	mes = 1
	capitalsum = capital * 0.1667
	suma = 0
	Mientras mes <= 12 Hacer
		capital = capital + capitalsum
		mes = mes + 1
	Fin Mientras
	Escribir capital
FinAlgoritmo
