from cuadrado import Cuadrado
from figuraGeometrica import FiguraGeometrica

# no es posible crear objetos de una clase abstracta
# figuraGeometrica= FiguraGeometrica()

cuadrado = Cuadrado(4, 'rojo')
print("Cuadrado: ", cuadrado)
print("Area del cuadrado: ", cuadrado.area())

print(Cuadrado.mro())