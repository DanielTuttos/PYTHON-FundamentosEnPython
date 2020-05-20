from producto import Producto
from orden import Orden

producto1 = Producto('leche', 12.90)
producto2 = Producto('cafe', 1.90)
producto3 = Producto('arroz', 17.75)
producto4 = Producto('azucar', 1.00)

productos = [producto1, producto3, producto4]

orden1 = Orden(productos)
print(orden1)
print(orden1.calcular_total())


# productos.append(producto2)
orden2 = Orden(productos)
orden2.agregar_producto(producto2)
print(orden2)
print(orden2.calcular_total())