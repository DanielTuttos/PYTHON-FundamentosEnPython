# break rompe por completo el ciclo que estamos ejecutando
# imprimir solo las letra a contenidas en una cadena
for letra in "Holanda":
    if(letra == "a"):
        print(letra)
        break

print("fin ciclo")


# numeros pares dentro de un rango
# for i in range(6):
#     if(i%2==0):
#         print(i)

# continue continia con la siguiente iteracion del ciclo for
for i in range(6):
    if(i % 2 != 0):
        continue
    
    print(i)
