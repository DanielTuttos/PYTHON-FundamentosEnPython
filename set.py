# set es una coleccion sin orden, y tampoco tienen indices ni elementos repetidos y los elementos no de pueden modificar pero si agregar nuevos y eliminar existentes
planetas = {'Jupiter', 'Marte', 'Venus'}
print(planetas)

# largo
print(len(planetas))

# revisar si un elemento esta presente
print('Marte' in planetas)

# agregar 
planetas.add('Tierra')
print(planetas)


planetas.add('Tierra') # no se pueden agregar elementos duplicados
print(planetas)

# eliminar con remove posiblemente arroja una excepcion 
planetas.remove('Tierra')
print(planetas)

# eliminar con discard que no arroja excepcion
planetas.discard('Jupiter')
print(planetas)

# limpiar el set
planetas.clear()
print(planetas)

# eliminar el set
del planetas