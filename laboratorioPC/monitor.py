class Monitor:
    contador_monitores = 0
    def __init__(self, marca, tamanio):
        Monitor.contador_monitores += 1
        self.__id_monitor = Monitor.contador_monitores
        self.__marca=marca
        self.__tamanio=tamanio
        
    def __str__(self):
        return (
            f'Id: {self.__id_monitor}, '
            f'Marca: {self.__marca}, '
            f'Tamanio: {self.__tamanio} pulgadas'
        )
        
# monitor = Monitor('lg', '14')
# print(monitor)