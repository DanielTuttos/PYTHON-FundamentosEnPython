import os


class CatalogoPeliculas:

    ruta_archivo = "peliculas.txt"

    @staticmethod
    def agregar_pelicula(pelicula):
        try:
            # a = modo append para conservar lo que ya existe
            archivo = open(CatalogoPeliculas.ruta_archivo, 'a')
            archivo.write(pelicula.__str__() + "\n")
        except Exception as e:
            print('ocurrio un error al agregar: ', e)
        finally:
            archivo.close()

    @staticmethod
    def listar_peliculas():
        try:
            archivo = open(CatalogoPeliculas.ruta_archivo, 'r')
            print('Catalogo de Peliculas: ')
            print(archivo.read())
        except Exception as e:
            print('ocurrio un error al listar peliculas: ', e)
        finally:
            archivo.close()

    @staticmethod
    def eliminar():
        try:
            os.remove(CatalogoPeliculas.ruta_archivo)
            print('archivo eliminado: ', CatalogoPeliculas.ruta_archivo)
        except Exception as e:
            print('ocurrio un error al eliminar peliculas: ', e)
