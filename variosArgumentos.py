from random import *

def suma_cuadrados(*cuadrados):
    cuadrado = 0
    for num in cuadrados:
        cuad= num*num
        cuadrado += cuad
    return cuadrado



def numeros_persona(nombre,*numeros):
    suma_numeros = 0
    for numero in numeros:
        respuesta=print(f"{nombre}, la suma de tus números es {suma_numeros}")
        suma_numeros += numero
    return respuesta
    
numeros_persona('Juan',list[1,5,3,7,2])
