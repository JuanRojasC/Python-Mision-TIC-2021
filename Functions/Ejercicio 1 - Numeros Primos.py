# crear un programa que iniciace una lista de n elementos con datos pedidos por el teclado
# cree una funcion y adicione en otra lista los numeros primos que estan dentro primera lista

print('\n\t\t\t\tHola Bienvenido\n\nAcontinuacion se te pedira que ingreses numeros para añadir a una lista')

# Entradas
estado = 1
lista = []

while estado == 1 :
    elemento = int(input('Ingrese un numero: '))
    lista.append(elemento)
    estado = int(input('Desea agregar otro numero si(1) no(0): '))


# Funciones
def numeroPrimo(array):
    numerosPrimos = []
    for i in array:
        primo = True
        for x in range(2,i):
            if i % x == 0:
                primo = False
        if primo == True and i != 0 and i != 1:
            numerosPrimos.append(i)
    return numerosPrimos


# Salidas
print('La lista de numeros es',lista,'\n')
print('Los numeros primos de la lista son',numeroPrimo(lista),'\n')