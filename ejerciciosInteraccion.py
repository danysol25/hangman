'''
from random import *

#dadoUno
def dado_uno():
    dadoUno = randint(1,6)
    return dadoUno

#dadoDos
def dado_dos():
    dadoDos = randint(1,6)
    return dadoDos

print(dado_uno())
print(dado_dos())

def lanzar_dados ():
    print(f'el primer dado arrojó {dado_uno}, y el segundo {dado_dos}. La suma de ambos es: {suma_dados}.')
    print(resultado)

#sumar dados
def suma_dados(uno, dos):
    resultado = uno + dos
    if resultado <= 6:
        print(f"La suma de tus dados es {suma_dados}. Lamentable")
    elif resultado > 6 and resultado < 10:
        print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    else: 
        print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")
    return resultado

print(suma_dados(dado_uno, dado_dos))

'''


'''
#CODIGO CORRECTO
import random
 
def lanzar_dados():
    return random.randint(1,6), random.randint(1,6)
 
def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

'''

#crear variable de lista de numeros 
lista_numeros = [1,2,15,7,2]
#escanear lista y ordenar (y elimino el más alto)
#eliminar repetidos
def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort()
    lista.pop(-1)
    return lista

def promedio(lista):
    promedio = sum(lista)/len(lista)
    return promedio

#Práctica sobre Interacción entre Funciones 3

lista_numeros = [1,2,15,7,2,8]
 
import random
 
def lanzar_moneda():
    resultado = random.choice(["Cara", "Cruz"])
    return resultado
 
def probar_suerte(moneda, lista):
    if moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    elif moneda == "Cruz":
        print("La lista fue salvada")
        return lista
