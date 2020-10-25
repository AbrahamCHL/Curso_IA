import psycopg2


class Postgres():
    def __init__(self):
        self.__conn = psycopg2.connect(host="localhost", port = 5432, database="postgres", user="admin", password="admin")
        self.__cur = self.__conn.cursor()

    def createTable(self,_sql):
        self.__cur.execute(_sql)
        # self.commit()
        
    def insert(self,_sql, _numeroPlazas):
        self.__cur.execute(_sql, (_numeroPlazas,_numeroPlazas,0))
        # self.commit()

    def selectSoloUno(self,_sql, _id):
        self.__cur.execute(_sql,(_id,))
        query_results = self.__cur.fetchall() 
        if len(query_results) > 0:
            self.__numeroPlazas = query_results[0][1]
            self.__plazasDisponibles = query_results[0][2]
            self.__plazasVendidas = query_results[0][3]
            return self.__numeroPlazas, self.__plazasDisponibles, self.__plazasVendidas
        else:
            return False

    def selectTodo(self,_sql):
        self.__cur.execute(_sql)
        query_results = self.__cur.fetchall()

        return query_results

    def update(self,_sql,plazas_disponibles,plazas_vendidas,id):
        
        self.__cur.execute(_sql, (plazas_disponibles,plazas_vendidas,id))
        # self.commit()
    
    def delete(self,_sql,_id):
       
        self.__cur.execute(_sql,(_id,))
        # self.commit()

    def closeConection(self):
        self.__cur.close()
        self.__conn.close()
    
    def commit(self):
        self.__conn.commit()
    


    


