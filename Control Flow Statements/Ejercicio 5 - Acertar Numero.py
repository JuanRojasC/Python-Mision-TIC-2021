# 5. Crear un programa que alamacene un numero y que lea un numero y diga si el numero es menor o es mayor al numero almacenado.

number = 50

# Entrada
inputnumber = float(input('ingrese un numero: '))


# Comprobacion
if inputnumber == number :
    print('Muy bien has acertado el numero')
else :
    if inputnumber > number :
        print('El numero es menor que el que ingresaste')
    else :
        print('El numero es mayor al que ingresaste')