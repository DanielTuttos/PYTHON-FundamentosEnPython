from figuraGeometrica import FiguraGeometrica
from color import Color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        # super().__init__(lado, lado)
        Color.__init__(self, color)
        
    def area(self):
        return self.get_alto() * self.get_ancho()
    
    def __str__(self):
        return super().__str__() + ', Color: '+ self.get_color()