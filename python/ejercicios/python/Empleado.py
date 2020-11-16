from Persona import Persona

class Empleado(Persona):
    
    def __init__(self, nombre, apellido, numero):
        Persona.__init__(self,nombre,apellido)
        self.numero = numero

    def __str__(self):
        return super().__str__() + ", "+self.numero


persona = Persona("Juan", "Pérez")
empleado = Empleado("Lucas", "Ramirez", "1007")

print(persona.__str__())
print(empleado.__str__())