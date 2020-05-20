from dominio.pelicula import Pelicula
from servicio.catalogoPeliculas import CatalogoPeliculas

opcion = None

while opcion != '4':
    print('Opciones: ')
    print('1. Agregar Pelicula')
    print('2. Listar Peliculas')
    print('3. Eliminar catalogo de Peliculas')
    print('4. Salir')
    opcion = input('Escribe tu opcion (1-4): ')
    if opcion == '1':
        nombre_pelicula = input('Proporciona el nombre de la pelicula: ')
        pelicula = Pelicula(nombre_pelicula)
        CatalogoPeliculas.agregar_pelicula(pelicula)
    elif opcion == '2':
        CatalogoPeliculas.listar_peliculas()
    elif opcion == '3':
        CatalogoPeliculas.eliminar()
else:
    print('Salimos del programa...')
