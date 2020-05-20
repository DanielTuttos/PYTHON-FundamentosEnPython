from empleado import Empleado
from gerente import Gerente

def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto), end="\n\n")
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado = Empleado('danny', 550.00)
imprimir_detalles(empleado)

empleado = Gerente('daniel', 3000.00, 'ventas')
imprimir_detalles(empleado)