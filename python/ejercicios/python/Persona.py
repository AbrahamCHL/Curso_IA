class Persona:
    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def __str__(self):
        return self.nombre + " "+ self.apellido
