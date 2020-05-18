class Persona:

    def __init__(this, n, e, *v, **d):
        this.nombre = n
        this.edad = e
        this.valores = v
        this.diccionario = d

    def desplegar(self):
        print('Nombre:', self.nombre)
        print('Edad:', self.edad)
        print('Valores (Tupla) :', self.valores)
        print('Diccionario:', self.diccionario)


p1 = Persona('daniel', 23)
p1.desplegar()
print()
p2 = Persona('juan', 37, 2, 4, 5, 6, 7)
p2.desplegar()
print()
p3 = Persona('Carolina', 37, 6, 7, m="maria", p="paola", c="carlos")
p3.desplegar()
