# mantiene el orden y no se puede modificar
frutas = ('Naranja','Platano','Guayaba')
print(frutas)

# largo de la tupla
print(len(frutas))

# accediento a un elemento 
print(frutas[2])

# navegacion inversa
print(frutas[-3])

# rango
print(frutas[0:2]) #excluyendo elindice 2

# modificar un valor
# frutas[0]="papaya"
frutasLista = list(frutas)
frutasLista[1] = "Platanito"
frutas = tuple(frutasLista)
print(frutas) 

# iterar una tupla
for fruta in frutas:
    print(fruta, end=" ")
    
# no podemos agregar nuevos elementos ni eliminar
del frutas
print (frutas)