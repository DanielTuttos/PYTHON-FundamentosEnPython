class Aritmetica:

    """Clase Artimetica para realizar las operaciones de sumar, restar, etc"""

    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    """Se realiza la operación con los atributos de la clase"""

    def sumar(self):
        return self.operando1 + self.operando2

    def restar(self):
        return self.operando1 - self.operando2

    def multiplicar(self):
        return self.operando1 * self.operando2

    def dividir(self):
        return self.operando1 / self.operando2


# creamos un nuevo objeto
numero1 = int(input('Ingrese el primer numero para las operaciones: '))
numero2 = int(input('Ingrese el segundo numero para las operaciones: '))
aritmetica = Aritmetica(numero1, numero2)
print('Resultado de la suma:', aritmetica.sumar())
print('Resultado de la resta:', aritmetica.restar())
print('Resultado de la multiplicacion:', aritmetica.multiplicar())
print('Resultado de la division:', aritmetica.dividir())


# creamos un nuevo objeto
# aritmetica2 = Aritmetica(10, 50)
# print('El resultado de la suma es:', aritmetica2.sumar())
# print('El resultado de la resta es:', aritmetica2.restar())
# print('El resultado de la multiplicacion es:', aritmetica2.multiplicar())
# print('el resultado de la division es:', aritmetica2.dividir())
