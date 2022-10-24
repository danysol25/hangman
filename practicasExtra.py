import random

def devolver_distintos(*parametros):
    if sum(parametros)>15:
        print(max(parametros))
    elif sum(parametros)<10:
        print(min(parametros))
    elif sum(parametros)>=10 and sum(parametros)<=15:
        print(sum(parametros)/len(parametros))

devolver_distintos(1,2,1,4)


def palabra_ordenada(palabra):
    mi_set= set()
    
    for letra in palabra:
        mi_set.add(letra)
        
    mi_lista = list(mi_set)
    mi_lista.sort()
    return mi_lista

print(palabra_ordenada('elefante'))


def doble_cero(*args):
    indice= 0
    for cero in args:
        if indice + 1 == len(args): #Cuando ya recorrió todo el bucle
            return False
        elif args[indice] == 0 and args[indice+1] == 0:
            return True
        else:
            indice +=1 #SUMA UNO AL INDICE PARA SEGUIR ITERANDO
    return False

print(doble_cero(5,6,1,0,0,9,3,5))
print(doble_cero(6,0,5,1,0,3,0,1))


hasta = int(input("Ingrese un número del 1 al 500: "))
def contar_primos(numero):
    primos = []
    iteracion = 3
    if numero<2:
        return 0

    while iteracion <= numero:
        for n in range (3,iteracion,2):
            if iteracion%n ==0:
                iteracion +=2
                break
        else:
            primos.append(iteracion)
            iteracion += 2
    print(primos)
    return len(primos)

print(contar_primos(50))    

contar_primos()
