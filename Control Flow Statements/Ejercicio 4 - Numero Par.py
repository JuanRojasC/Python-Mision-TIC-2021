# 4. Ingresar un numero y mostrar si el numero es par o es impar

# Entrada
numero = float(input('Ingrese un numero: '))


# Comprobacion
if numero % 2 == 0 :
    print('El numero {} es par'.format(numero))
else :
    if numero == 0 :
        print('El numero es 0')
    else : 
        print('El numero {} es impar'.format(numero))