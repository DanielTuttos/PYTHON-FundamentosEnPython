# from modulos import moduloAritmetica as aritmetica // desde otra carpeta
import modulos.moduloAritmetica as aritmetica # desde mismo nivel

print ('la suma es: ', aritmetica.sumar(3, 4))
print ('la resta es: ', aritmetica.resta(10, 4))