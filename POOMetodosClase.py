class MiClase:

    variable_clase = 'variable clase'

    def __init__(self):
        self.variable_instancia = 'variable instancia'

    @staticmethod
    def metodo_estatico():
        print('metodo estatico')
        print(MiClase.variable_clase)
        # desde un metodo statico no podemos acceder a una variable de instancia
        # print(MiClase.variable_instancia)

    @classmethod
    def metodo_clase(cls):
        print('metodo de clase: ' + str(cls))
        print(cls.variable_clase)

        # no podemos acceder a la variable de instancia desde contexto estatico
        # print(cls.variable_instancia)

    def metodo_instancia(self):
        self.metodo_estatico()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)


MiClase.metodo_estatico()
MiClase.metodo_clase()

print()
objeto1 = MiClase()
objeto1.metodo_instancia()
