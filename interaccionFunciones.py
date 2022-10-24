#cuando una función le pasa datos a otra.
from random import shuffle
#Lista inicial
palitos = ['-','--','---','----']

#mezclar palitos
#shuffle(palitos) NO SE PUEDE INVOCAR ASÍ, PORQUE NO DEVUELVE NADA. No puedo ponerlo en una variable, debe ser parte de una función.
def mezclar(lista):
    shuffle(lista)
    return lista

#preguntar al usuario qué palito
def probar_suerte():
    intento= ''
    while intento not in range(1,5):
        intento = int(input('Elige un número del 1 al 4:'))
    return intento

intento1= probar_suerte() #defino el intento llamándo a la función
print(intento1)

#comprobar intento
def chequear_intento(lista, intento):
    if lista[intento -1] == '-':
        print('Toca lavar los platos')
    else:
        print('Eximido de tareas.')
    
    print(f'Te ha tocado {lista[intento-1]}.')
#tarea asignada según el palito obtenido

#interacción de funciones
palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)


    
