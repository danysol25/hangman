from random import *
def suma(**kwargs):
    total=0
    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}.')
        total += valor
    return total

print(suma(x=3,y=5,z=2)) #esto NO es un diccionario, pero al ser pares, el programa lo reconoce como tal KEY-VALUE



#MEZCLAR ARGUMENTOS:
def prueba(num1,num2,*argumentos,**kwordargs):
    print(f'El primer parámetro es:{num1}.')
    print(f'El segundo parámetro es:{num2}.')

    for argum in argumentos:
        print(f'Uno de los argumentos es: {argum}.')
    
    for clave,valor in kwordargs.items():
        print(f'Uno de los kwargs es: {clave} = {valor}.')

prueba(15,'azul',200,4,50,'doctor','perro',j=15,k='dieciseis',l=17)


#Práctica sobre Argumentos Indefinidos (*args) 2
def suma_absolutos(*todos):
    suma=0
    for num in todos: #escaneo todos los argumentos
        absoluto = abs(num) #convierto a absoluto todos los números
        suma += absoluto #sumo todos
    return suma


#Práctica sobre Argumentos Indefinidos (*args) 3

def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f'{nombre}, la suma de tus números es {suma_numeros}'

#es lo mismo que mi código:
def numeros_persona(nombre,*numeros):
    suma_numeros = 0
    for numero in numeros:
        suma_numeros += numero
    return f"{nombre}, la suma de tus números es {suma_numeros}"

#Práctica sobre Argumentos Indefinidos (*kwargs) 1

def cantidad_atributos(**kwargs):
    cantidad = 0
    for clave in kwargs.items():
        cantidad += 1
    return cantidad
#es lo mismo que:
def cantidad_atributos(**kwargs):
    for atri in kwargs:
        total = len(kwargs.items())
    return total

#Práctica sobre Argumentos Indefinidos (*kwargs) 2

def lista_atributos(**kwargs):
    lista = []
    for valor in kwargs.values():
        lista.append(valor)
    return lista

#Práctica sobre Argumentos Indefinidos (*kwargs) 3

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')
