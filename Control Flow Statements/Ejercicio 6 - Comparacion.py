# 6. que lea dos numero y muestre si los dos numeros leidos son: iguales o el primero es mayor que e segundo o el segundo mayor que el primero.

# Entradas
number1 = float(input('Ingrese el primer numero: '))
number2 = float(input('Ingrese el segundo numero: '))


# Comparacion
if number1 == number2 :
    print('Ambos numeros son iguales')
else :
    if number1 > number2 :
        print('El numero {} es mayor que el numero {}'.format(number1, number2))
    else :
        print('El numero {} es menor que el numero {}'.format(number1, number2))
