from nimeroIgualesException import NumerosIdenticosException
resultado = None

try:
    a = int(input('Primer numero: '))
    b = int(input('Segundo numero: '))
    if(a==b):
        raise NumerosIdenticosException('ocurrio un error,numeros identicos')
    resultado = a/b
except ZeroDivisionError as e:
    print('ocurrio un error con ZeroDivisionError ', e)
    print(type(e))
except TypeError as e:
    print('ocurrio un error con TypeError ', e)
    print(type(e))
except Exception as e:
    print('ocurrio un error con Exception ', e)
    print(type(e))
else:
    print('no hubo ninguna exception')
finally:
    print('fin del manejo de excepciones')
    
print('resultado: ', resultado)

print('continuando............')
