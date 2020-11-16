precio_original = input("Introducir el precio original: ")
precio_final = input("Introducir el precio final pagado: ")

cantidad = int(precio_final) - int(precio_original)
porcentaje = int(cantidad) * 100 / int(precio_original)
print("Cantidad que ha pagado de mas: "+str(cantidad)+"\nPorcentaje: "+str(porcentaje))