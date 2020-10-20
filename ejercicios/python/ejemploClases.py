class Perro:
    def __init__(self,pNombre):
        self.__nombre = pNombre
    
   
    def SetNombre(self, pNombre):
        self.__nombre = pNombre

    def GetNombre(self):
        return self.__nombre

perro1 = Perro("")
perro1.SetNombre("COS")
print(perro1.GetNombre())


