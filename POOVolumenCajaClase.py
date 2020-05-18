class Caja:
    
    def __init__(self, alto, ancho, profundo):
        self.ancho=ancho
        self.profundo=profundo
        self.alto=alto
        
    def calcularVolumenCaja(self):
        volumen = self.profundo * self.ancho * self.alto
        return volumen
    
print('Calcular el volumen de una caja')

alto=int(input('Ingrese el alto de la caja: '))
ancho=int(input('Ingrese el ancho de la caja: '))
profundo=int(input('Ingrese la profundidad de la caja: '))

volumen = Caja(alto, ancho, profundo)
print ('El volumen de la caja es: ',volumen.calcularVolumenCaja(), 'm')