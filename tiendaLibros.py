print("Proporcione los siguientes datos del libro:")
nombre = input("Proporciona el nombre:")
id = int(input("Proporciona el ID:"))
precio = float(input("Proporcione el precio:"))
envioGratuito = input("Indica si el envio es gratuito (True/False):")

if envioGratuito == "True" or envioGratuito == "true":
    envioGratuito = True
elif envioGratuito == "False" or envioGratuito == "false":
    envioGratuito = False
else:
    envioGratuito = "Valor incorrecto, debe ser True/False"    

print("Nombre:", nombre)
print("Id:", id)
print("Precio:", precio)
print("Envío Gratuito?:", envioGratuito)   

print(type(envioGratuito)) 