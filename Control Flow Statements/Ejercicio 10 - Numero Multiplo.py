comprobacion = [0,0]

# Entrada de numero
numero1 = int(input('Ingrese el primer numero: '))
numero2 = int(input('Ingrese el segundo numero: '))

# Comprobacion de multiplo
if numero1 % numero2 == 0 :
    comprobacion[0] = True
if numero2 % numero1 == 0 :
    comprobacion[1] = True
if numero1 % numero2 != 0 :
    comprobacion[0] = False
if numero2 % numero1 != 0 :
    comprobacion[1] = False

# Impresion
if comprobacion[0] == True :
    print('El ', numero1, ' es multiplo de ', numero2)
elif comprobacion[1] == True :
    print('El ', numero2, ' es multiplo de ', numero1)
elif comprobacion[0] == False :
    print('El ', numero1, 'no es multiplo de ', numero2)
elif comprobacion[1] == False :
    print('El ', numero2, 'no es multiplo de ', numero1)

