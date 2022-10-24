def saludar() : 
    print("¡Hola mundo!")

nombre_persona=''
def bienvenida (nombre_persona):
    print(f"¡Bienvenido {nombre_persona}!")

#RETURN
a=3
b=8
def potencia (a,b):
    return(a**b)

dolares=10
def usd_a_eur(valor):
    return(valor*0.90)

#INVERTIR EL ORDEN
palabra='palabra'
def invertir_palabra(palabra):
    palabra = palabra[::-1]
    palabra = palabra.upper()
    return palabra