class MyClase:

    variable_clase = "Variable de clase"

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

print (MyClase.variable_clase)
objeto1 = MyClase('valor variable instancia')
MyClase.variable_instancia = 'modificado'
print (MyClase.variable_instancia) # valores distintos
print (objeto1.variable_instancia) # valores distintos

# podemos acceder a las variables de clase desde los objetos
print(objeto1.variable_clase)
# podemos acceder a las variables de clase con el nombre de la clase
print(MyClase.variable_clase)

objeto1.variable_clase = 'modificando variable de clase'
print(objeto1.variable_clase)
print(MyClase.variable_clase)


objeto2 = MyClase('nuevo valor de variable de instancia')
print(objeto2.variable_clase)

objeto3=MyClase('tercer objeto')

MyClase.variable_clase = 'cambio desde la clase'
print(objeto1.variable_clase)
print(objeto2.variable_clase)
print(MyClase.variable_clase)