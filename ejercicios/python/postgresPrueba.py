import psycopg2
from tkinter import *


root = Tk()

 
root.title("Hola mundo")     
root.resizable(0, 150) 
root.geometry("120x200")

conn = psycopg2.connect(host="localhost", port = 5432, database="postgres", user="postgres", password="postgres")


cur = conn.cursor()

cur.execute("""SELECT col1, col2, col3 FROM public.hola""")
query_results = cur.fetchall()
print(query_results)
label = Label(root, text= query_results)
label.pack() 


root.mainloop() 
cur.close()
conn.close()