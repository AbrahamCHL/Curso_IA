a = input("Introduce el primer numero: ")
b = input("Introduce el segundo numero: ")
c = input("Introduce el tercer numero: ")

if a > b and a > c:
    print(str(a)+" es el mayor de los tres")
elif b > a and b > c:
    print(str(b)+" es el mayor de los tres")

elif c > b and c > a:
    print(str(c)+" es el mayor de los tres")
