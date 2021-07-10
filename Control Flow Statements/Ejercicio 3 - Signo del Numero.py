# 3. Ingresar un numero y mostrar si el numero es positivo, negativo o cero

# Entradas
numero = float(input('ingrese un numero: '))


# Comprobacion
if numero > 0 :
    print('El numero es positivo')
else :
    if numero == 0 :
        print('El numero es 0')
    else :
        print('El numero es negativo')