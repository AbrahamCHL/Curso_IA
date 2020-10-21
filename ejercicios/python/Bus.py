class Bus():
    def __init__(self,numeroPlazas):
        self.__numeroplazas = numeroPlazas
        self.__plazas_disponibles = numeroPlazas

    def getNumeroPlazas(self):
        return self.__numeroplazas

    def getPlazasDisponibles(self):
        return self.__plazas_disponibles
    
    def ventaDeBilletes(self,billetesAcomprar):
        ventacorrecta = False
        if billetesAcomprar > self.getPlazasDisponibles():
            #ventacorrecta = False
            pass
        
        else:
            self.__plazas_disponibles -= billetesAcomprar
            ventacorrecta = True

        return ventacorrecta
        
    def devolucion(self,BilletesADevolver):
        devolucioncorrecta = False
        if self.getNumeroPlazas() < (BilletesADevolver + self.getPlazasDisponibles()):
            #devolucioncorrecta = False
            pass
        
        else:
            self.__plazas_disponibles += BilletesADevolver
            devolucioncorrecta = True
        return devolucioncorrecta
    
    def billetesVendidos(self):
        return self.getNumeroPlazas() - self.getPlazasDisponibles()


