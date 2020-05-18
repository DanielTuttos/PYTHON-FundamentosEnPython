class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


# modificar los valores
Persona.nombre = 'daniel'
Persona.edad = 23

# acceder a los valores
print(Persona.nombre)
print(Persona.edad)

# creacion de un objeto
persona = Persona('karla', 43)
print(persona.nombre)
print(persona.edad)
print(id(persona))

# creando un segundo objeto
persona2 = Persona('jonathan', 43)
print(persona2.nombre)
print(persona2.edad)
print(id(persona2))