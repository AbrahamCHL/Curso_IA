class Bus():
    def __init__(self,numeroPlazas):
        self.setNumeroPlazas(numeroPlazas)
        self.plazas_disponibles = numeroPlazas

    
    def getPlazasDisponibles(self):
        return self.plazas_disponibles

    def getNumeroPlazas(self):
        return self.numeroplazas

    def getPlazasDisponibles(self):
        return self.plazas_disponibles
    
    def setNumeroPlazas(self,nPlazas):
        self.numeroplazas = nPlazas
    
    def ventaDeBilletes(self,billetesAcomprar):
        self.plazas_disponibles -= billetesAcomprar
        

    def devolucion(self,BilletesADevolver):
        self.plazas_disponibles += BilletesADevolver

    
    def billetesVendidos(self):
        self.billetes_vendidos = self.getNumeroPlazas() - self.getPlazasDisponibles()
        return self.billetes_vendidos