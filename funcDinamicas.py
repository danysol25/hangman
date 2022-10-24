#Función para buscar positivos en una lista
def todos_positivos(lista_numeros):
    for numero in lista_numeros:
        if numero < 0:
            return False
        else:
            pass
    return True


#Función para sumar pares en un rango
def suma_menores(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero in range(0,1000):
            suma += numero
        else:
            pass
    return suma

lista_numeros = [1,-50,502,-5000,755,600,33,61]


#trabajar con TUPLAS
#enuncio una tupla, por ejemplo.
precios_cafe = [('capuchino',1.5), ('Latte',2.2), ('Americano', 1.10)]

#defino la funcion con parametro
def cafe_mas_caro(lista_precios):
    precio_mayor= 0 #inicializo las variables involucradas en el mín valor.
    cafe_mas_caro = ''

    for cafe, precio in lista_precios: #itero valor 1 y valor 2 dentro de mi tupla.
        if precio > precio_mayor: #comparo valores
            precio_mayor = precio #cuando el valor es >, reemplaza al valor anterior
            cafe_mas_caro = cafe #una vez ya definido cuál es ese valor >, le asocio el valor 2 del conjunto.
        else:
            pass

    return(cafe_mas_caro,precio_mayor) #retorna la pareja tupla

cafe, precio = cafe_mas_caro(precios_cafe)
print(f'El cafe más caro es {cafe}, que tiene el costo de {precio}.')