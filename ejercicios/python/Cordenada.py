class Cordenada:
    def __init__(self, x, y):
        self.SetX(x)
        self.SetY(y)
    
    def SetX(self,cordx):
        self.x = cordx

    def SetY(self,cordy):
        self.y = cordy

    def GetX(self):
        return self.x
    
    def GetY(self):
        return self.y