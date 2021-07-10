# 2  Crear un programa que lea n cantidad de numeros y muestre la tabla de multiplicar de de los numeros pares leidos
estado = 1

while estado == 1 :
    numero = int(input('Ingrese un numero: '))
    if numero % 2 == 0 :
        print('La tabla del numero',numero)
        for x in range (1,11) :
            print(numero,'x',x,'=',numero*x)
    else :
        estado = int(input('Desea agregar otro numero si(1) no(0): '))