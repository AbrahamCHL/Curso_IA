# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="password",
        host="172.24.0.1",
        port=3306,
        database="prueba"

    )
    cur = conn.cursor()

    cur.execute("SELECT * FROM personas")

    for (id, nombre) in cur:
        print(f"id: {id}, nombre: {nombre}")

    conn.close()
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
