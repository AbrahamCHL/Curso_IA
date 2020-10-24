import psycopg2


class Postgres():
    def __init__(self):
        self.__conn = psycopg2.connect(host="localhost", port = 5432, database="postgres", user="admin", password="admin")
        self.__cur = self.__conn.cursor()

    def createTable(self,nameTable):
        sql ="""CREATE TABLE IF NOT EXISTS public.{}
            (
                ID SERIAL PRIMARY KEY,
                NUMERO_PLAZAS integer NOT NULL,
                PLAZAS_DISPONIBLES integer,
                PLAZAS_VENDIDAS integer
            )""".format(nameTable)
        self.__cur.execute(sql)
        self.commit()
        # self.closeConection()
        
    def insert(self,numeroPlazas):
        sql = """INSERT INTO public.bus(
            numero_plazas, plazas_disponibles, plazas_vendidas)
            VALUES (%s,%s,%s)"""
        self.__cur.execute(sql, (numeroPlazas,numeroPlazas,0))
        self.commit()
        # self.closeConection()

    def selectSoloUno(self,id):
        sql ="""SELECT id, numero_plazas, plazas_disponibles, plazas_vendidas
	    FROM public.bus WHERE id = %s"""
        self.__cur.execute(sql,(id,))
        query_results = self.__cur.fetchall()
        self.__numeroPlazas = query_results[0][1]
        self.__plazasDisponibles = query_results[0][2]
        self.__plazasVendidas = query_results[0][3]
        return self.__numeroPlazas, self.__plazasDisponibles, self.__plazasVendidas
    
    def selectTodo(self):
        sql ="""SELECT id, numero_plazas, plazas_disponibles, plazas_vendidas
	    FROM public.bus """
        self.__cur.execute(sql)
        query_results = self.__cur.fetchall()

        return query_results

    def update(self,plazas_disponibles,plazas_vendidas,id):
        sql = """UPDATE public.bus SET plazas_disponibles = (%s),
            plazas_vendidas = (%s) WHERE id = (%s)""" 
        self.__cur.execute(sql, (plazas_disponibles,plazas_vendidas,id))
        self.commit()
    
    def delete(self,id):
        psql ="""DELETE FROM public.bus WHERE id = %s"""
        self.__cur.execute(sql,(id,))

    def closeConection(self):
        self.__cur.close()
        self.__conn.close()
    
    def commit(self):
        self.__conn.commit()
    


    


