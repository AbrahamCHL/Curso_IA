import psycopg2
from tkinter import *


# root = Tk()
# root.title("Hola mundo")     
# root.resizable(0, 150) 
# root.geometry("120x200")

conn = psycopg2.connect(host="localhost", port = 5432, database="postgres", user="admin", password="admin")


cur = conn.cursor()

# sql ="""CREATE TABLE IF NOT EXISTS public.bus 
# (
#     ID SERIAL PRIMARY KEY,
#     NUMERO_PLAZAS TEXT NOT NULL,
#     PLAZAS_DISPONIBLES integer NOT NULL,
#     PLAZAS_VENDIDAS integer NOT NULL
# )"""

sql = """INSERT INTO public.bus(
	numero_plazas)
	VALUES (%s)"""
# cur.execute("""SELECT * income FROM public.bus""")
cur.execute(sql, (7,))
# cur.execute(sql)
# query_results = cur.fetchall()
# print(query_results)
# label = Label(root, text= query_results)
# label.pack() 
conn.commit()

# root.mainloop() 
cur.close()
conn.close()