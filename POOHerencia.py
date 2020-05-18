class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return 'Nombre: ' + self.nombre + ', edad: '+ str(self.edad)


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)  # inicializa los valores de la clase padre
        self.sueldo = sueldo
        
    def __str__(self):
        return super().__str__() + ', sueldo: ' + str(self.sueldo)
        
persona = Persona('daniel', 34)
print(persona)

empleado = Empleado('jonathan', 54, 1209.00)
print(empleado)