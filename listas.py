nombres = ['Adrian', 'Luis', 'Carla', 'Ricardo', 'Maria']
print(nombres)

# largo de la lista
print(len(nombres))

# elemento 0
print(nombres[4])
print(nombres[1])

# navegacion inversa
print(nombres[-1])
print(nombres[-2])

# imprimir rango
print(nombres[0:2])  # sin incluir el indice 2

# imprimir los elementos de inicio hasta el indice proporcionado
print(nombres[:3])  # sin incluir el indice 3

# imprimir los elementos hasta el final desde el inidice proporcionado
print(nombres[1:])

# cambiar los elementos de una lista
nombres[4] = "Ivonne"
print(nombres)

# iterar las listas
for nombre in nombres:
    print(nombre)
    
# revisar si un elemento existe en la lista
if "Ricardo" in nombres:
    print("Si existe el nombre ricardo")
else:
    print("no existe el nombre")
    
# agregar un nuevo elemento a la lista
nombres.append("Jonathan")
print(nombres)

# insertar un nuevo elemento en elindice proporcionado
nombres.insert(1, "Eva")
print (nombres)

# remover un elemento
nombres.remove("Eva")
print(nombres)

# remover el ultimo elemento de la lista
nombres.pop()
print(nombres)

# remover el indice indicado de la lista
del nombres[0]
print(nombres)

# limpiar los elemento 
nombres.clear()
print(nombres)

# eliminar por completo la lista
# del nombres
# print(nombres)