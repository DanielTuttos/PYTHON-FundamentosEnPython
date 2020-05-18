class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        area = self.base * self.altura
        return area

print('Calcular el area de un rectangulo')

base = int(input('Ingrese la base de su rectangulo: '))
altura = int(input('Ingrese la altura de su rectangulo: '))

calcular = Rectangulo(base, altura)

print('El area del rectangulo es: ', calcular.calcularArea())