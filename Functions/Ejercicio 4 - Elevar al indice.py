# crear un programa lea un numero n y cree una lista los numeros leidos deben de estar entre 1 y 9, cree otra lista y una funcion
# y en la nueva lista dejar el numero de la primera lista elevado al indice de la nueva lista.
# eje: lista1=[1,5,6], nueva lista [1,5,36] no se debe utilizar pow y **.

# Entradas
estado = 1
lista = []

while estado == 1:
    numero = int(input('Ingrese un numero entre el 1 y el 9: '))
    while numero < 1 and numero > 9 :
        numero = int(input('<ERROR> Ingrese un numero valido entre 1 y 9: '))

    lista.append(numero)

    estado = int(input('Desea agregar otro numero si(1) no(0): '))
    while estado != 0 and estado != 1:
        estado = int(input('<ERROR> Ingrese un numero valido si(1) no(0): '))

# Funciones
def elevarNumeros(array):
    numerosElevados = []
    for posicion in range(len(array)):
        numeroElevado = 1
        for exponente in range(posicion):
            numeroElevado = numeroElevado * array[posicion]
        numerosElevados.append(numeroElevado)
    return numerosElevados


# Salidas
print('La lista de numeros es',lista)
print('La lista de numero elevado a su indice es',elevarNumeros(lista))
