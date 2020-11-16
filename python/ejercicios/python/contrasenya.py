comprobacion = True
contrasenyaCorrecta = False
while contrasenyaCorrecta == False:
    contrasenya = input("Introducir contraseña: ")
    # print(contrasenya)
    comprobacion = True
    while comprobacion == True:
        if len(contrasenya)>=7:
            # print("La contrasenya tiene 7 o mas letras")
            if contrasenya[0] in "AEIOU":
                # print("El primer caracter es una vocal mayuscula")
                if contrasenya[-1] in "0123456789":
                    # print("El ultimo caracter es un numero")
                    comprobacion = False
                    contrasenyaCorrecta = True
                    
                else:
                    print("El ultimo caracter no es un numero")
                    comprobacion = False
                    
            else:
                print("El primer caracter no es vocal mayuscula")
                comprobacion = False
                
        else:
            print("La contrasenya no tiene mas 7 letras")
            comprobacion = False



# print("Salistes")



