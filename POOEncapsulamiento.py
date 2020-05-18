class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):  # para obtener el valor del atributo privado y lo regresa
        return self.__nombre

    def set_nombre(self, nombre):  # para modificar el valor del atributo privado
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        self.__edad = edad


p1 = Persona('daniel', 18)
# print(p1.__nombre)
print(p1.get_nombre())
print(p1.get_edad())

# p1.__nombre = 'Alberto' error
p1.set_nombre('alberto')
p1.set_edad(100)
print(p1.get_nombre())
print(p1.get_edad())

