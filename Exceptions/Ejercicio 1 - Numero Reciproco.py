# crear un una funcion reciproca que imprima reciproco del numero que llego, ej. 3 el reciproco de 3 es 1/3 de 
# la funcion debe recibir una lista e imprimir el reciproco de cada numero que llega ej. ([3,0,a,4,5]).
# Utilizando excepciones controlar los errores que se presenten para que no se bloquee el programa. 
# y controlar los errores y co excepciones

# Funciones
def verificarNumero(numero):
    try:
        numero = int(numero)
    except ValueError:
        try:
            numero = float(numero)
        except ValueError:
            numero = 'ERROR'
    return numero

def reciproco(lista):
    listaReciprocos = []
    for elem in lista:
        if elem == 0:
            continue
        elif type(elem) == float:
            numero = str(elem).split('.')
            entero = numero[0]
            decimal = numero[1]
            potenciaDiez = '1'
            for x in range(len(decimal)):
                potenciaDiez += '0'
            reciproco = (int(entero) * int(potenciaDiez)) + int(decimal)
            reciproco = f'{potenciaDiez} / {str(reciproco)}'
            listaReciprocos.append(reciproco)
        else:
            reciproco = f'1 / {elem}'
            listaReciprocos.append(reciproco)
    return listaReciprocos


# Variables
listaNumeros = []

# Entradas
while True:
    numeroIngresado = verificarNumero(input('\nIngrese un numero: '))
    while numeroIngresado == 'ERROR':
        numeroIngresado = verificarNumero(input('\tIngrese un numero valido: '))
    listaNumeros.append(numeroIngresado)
    
    estado = input('\nDesea añadir otro numero si(1) no(0): ')
    while estado != '0' and estado != '1':
        estado = input('\tIngrese una opcion valida: ')
    if estado == '0':
        break

print(listaNumeros)
print(reciproco(listaNumeros))