from Persona import Persona

class Empleado(Persona):
    
    def __init__(self, nombre, apellido, numero):
        Persona.__init__(self,nombre,apellido)
        self.numero = numero

    def GetEmpleado(self):
        return self.Nombre() + ", "+self.numero


persona = Persona("Juan", "Pérez")
empleado = Empleado("Lucas", "Ramirez", "1007")

print(persona.Nombre())
print(empleado.GetEmpleado())