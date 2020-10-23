class Persona:
    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def Nombre(self):
        return self.nombre + " "+ self.apellido