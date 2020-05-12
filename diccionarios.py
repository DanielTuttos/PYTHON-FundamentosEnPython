# un diccionario esa compuesto de llave, valor (key, value)
diccionario={
    'IDE': 'Integrated Development Enviroment',
    'OOP': 'Object Oriented Programing',
    'DBMS': 'Database Management System'
}
print(diccionario)

# largo
print(len(diccionario))

# accedes a un elemento
print(diccionario['OOP'])

# OTRA FORMA
print(diccionario.get('DBMS'))

# modificando valores
diccionario['IDE'] = 'Integrated development enviroment'
print(diccionario)

# iterar
for termino in diccionario:
    print(termino)
    
for termino in diccionario:
    print(termino,':',diccionario[termino])

for valor in diccionario.values():
    print(valor)
    
# comprobar existencia de vlor
print('OOP' in diccionario)

# agregar nuevos elementos
diccionario['PK'] = 'Primary Key'
print(diccionario)

# remover elementos
diccionario.pop('DBMS')
print(diccionario)

# limpiar
diccionario.clear()
print(diccionario)

# eliminar el diccionario
del diccionario