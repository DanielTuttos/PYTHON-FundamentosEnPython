from orden import Orden
from computadora import Computadora
from monitor import Monitor
from teclado import Teclado
from raton import Raton

tecladoHP = Teclado('hp', 'usb')
ratonHP = Raton('hp', 'usb')
monitorHP = Monitor('hp', '27')
computadoraHP = Computadora('hp', monitorHP, tecladoHP, ratonHP)

tecladoAcer = Teclado('acer', 'wireless')
ratonAcer = Raton('acer', 'usb')
monitorAcer = Monitor('acer', '32')
computadoraAcer = Computadora('acer', monitorAcer, tecladoAcer, ratonAcer)

tecladoMSI = Teclado('MSI', 'usb')
ratonMSI = Raton('MSI', 'usb')
monitorMSI = Monitor('MSI', '40')
computadoraMSI = Computadora('acer', monitorMSI, tecladoMSI, ratonMSI)

computadoraArmada = Computadora('Armada', monitorMSI, tecladoHP, ratonAcer)

computadoras1 = [computadoraHP, computadoraAcer]
orden1 = Orden(computadoras1)
orden1.agregar_computadora(computadoraArmada)
print(orden1)

computadoras2 = [computadoraArmada, computadoraMSI, computadoraAcer]
orden2 = Orden(computadoras2)
print(orden2)