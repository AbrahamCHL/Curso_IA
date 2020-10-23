class Coordenada:
    def __init__(self, x, y):
        self.SetX(x)
        self.SetY(y)
    
    def SetX(self,cordx):
        self.__x = cordx

    def SetY(self,cordy):
        self.__y = cordy

    def GetX(self):
        return self.__x
    
    def GetY(self):
        return self.__y