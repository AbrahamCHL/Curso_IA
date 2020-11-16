# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="password",
        host="172.18.0.1",
        port=3306,
        database="prueba"

    )
    

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()
print("Primera SQL")
try:
    cur.execute("SELECT * FROM persona")
    for (id, nombre, apellido, edad) in cur:
        print(f"id: {id}, nombre: {nombre}, apellido: {apellido}, edad: {edad}")
except mariadb.Error as e:
    print(e)
    sys.exit(1)

print("Segunda SQL")

try:
    cur.execute("SELECT id,nombre FROM persona")
    for (id, nombre) in cur:
        print(f"id: {id}, nombre: {nombre}")
except mariadb.Error as e:
    print(e)
    sys.exit(1)

print("Tercera SQL")

try:
    cur.execute("SELECT * FROM persona WHERE edad > 20")
    for (id, nombre, apellido, edad) in cur:
        print(f"id: {id}, nombre: {nombre}, apellido: {apellido}, edad: {edad}")
except mariadb.Error as e:
    print(e)
    sys.exit(1)

print("Cuarta SQL")

try:
    cur.execute("SELECT * FROM persona WHERE edad > 20 and nombre like 'Karla'")
    for (id, nombre, apellido, edad) in cur:
        print(f"id: {id}, nombre: {nombre}, apellido: {apellido}, edad: {edad}")
except mariadb.Error as e:
    print(e)
    sys.exit(1)

print("Quinta SQL")

try:
    cur.execute("SELECT * FROM persona WHERE edad > 20 and nombre like '%br%'")
    for (id, nombre, apellido, edad) in cur:
        print(f"id: {id}, nombre: {nombre}, apellido: {apellido}, edad: {edad}")
except mariadb.Error as e:
    print(e)
    sys.exit(1)


print("Sexta SQL")

try:
    cur.execute("SELECT * FROM persona ORDER BY edad")
    for (id, nombre, apellido, edad) in cur:
        print(f"id: {id}, nombre: {nombre}, apellido: {apellido}, edad: {edad}")
except mariadb.Error as e:
    print(e)
    sys.exit(1)


print("Septima SQL")

try:
    cur.execute("SELECT * FROM persona ORDER BY edad DESC")
    for (id, nombre, apellido, edad) in cur:
        print(f"id: {id}, nombre: {nombre}, apellido: {apellido}, edad: {edad}")
except mariadb.Error as e:
    print(e)
    sys.exit(1)

conn.close()
