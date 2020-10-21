class Bus():
    def __init__(self,numeroPlazas):
        self.numeroplazas = numeroPlazas
        self.plazas_disponibles = numeroPlazas

    def getNumeroPlazas(self):
        return self.numeroplazas

    def getPlazasDisponibles(self):
        return self.plazas_disponibles
    
    def ventaDeBilletes(self,billetesAcomprar):
        ventacorrecta = False
        if billetesAcomprar > self.getPlazasDisponibles():
            #ventacorrecta = False
            pass
        
        else:
            self.plazas_disponibles -= billetesAcomprar
            ventacorrecta = True

        return ventacorrecta
        
    def devolucion(self,BilletesADevolver):
        devolucioncorrecta = False
        if self.getNumeroPlazas() < (BilletesADevolver + self.getPlazasDisponibles()):
            #devolucioncorrecta = False
            pass
        
        else:
            self.plazas_disponibles += BilletesADevolver
            devolucioncorrecta = True
        return devolucioncorrecta
    
    def billetesVendidos(self):
        self.billetes_vendidos = self.getNumeroPlazas() - self.getPlazasDisponibles()
        return self.billetes_vendidos


