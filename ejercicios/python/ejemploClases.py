class Perro:
    def __init__(self, pNombre):
        self.nombre = pNombre

    def DecirNombre(self):
        print("Mi nombre es: "+ self.nombre)
    
    def probando(self):
        print("QUe paso")

perro1 = Perro("Pascual")
perro1.DecirNombre()
perro1.probando()