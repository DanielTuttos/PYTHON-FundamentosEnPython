class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return 'Color: ' + self.color + ', ruedas: ' + str(self.ruedas)


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + ', velocidad: ' + str(self.velocidad) + 'km/h'


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ', Tipo: ' + self.tipo


vehiculo = Vehiculo('Rojo', 4)
print(vehiculo)

coche = Coche('Azul', 4 , 200 )
print(coche)

bicicleta = Bicicleta('Verde', 2, 'Montaña')
print(bicicleta)
