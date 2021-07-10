# crear un programa que iniciace una lista de n elementos con datos pedidos por el teclado
# cree una funcion y adicione en otra lista los numeros pares que estan dentro primera lista

# Entradas
estado = 1
lista =  []

while estado == 1:
    numero = int(input('Ingrese un numero: '))
    lista.append(numero)
    estado = int(input('Desea agregar otro numero si(1) no(0): '))
    while estado != 0 and estado != 1:
        estado = int(input('<ERORR> Ingrese una opcion valida si(1) no(0): '))
    

# Funciones
def numerosPares(array):
    numerosPares = []
    for i in array:
        if i % 2 == 0 and i != 0:
            numerosPares.append(i)
    return numerosPares


# Salidas
print('La lista de numeros es',lista,'\n')
print('Los numeros pares de la lista son',numerosPares(lista))