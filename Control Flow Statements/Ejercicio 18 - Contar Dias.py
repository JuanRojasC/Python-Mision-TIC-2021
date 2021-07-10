# 9. Construya un programa que calcule el número de días de un mes, dados los valores numéricos del mes y el año.

mes = int(input('Ingresa en numeros el mes (enero = 1): '))
año = int(input('Ingrese el año: '))

# Año bisiesto?
if año % 400 == 0 or (año % 4 == 0 and año % 100 != 0) :
    añoBisiesto = True
else :
    añoBisiesto = False


# Comprobacion
if mes in (1,3,7,8,10,12) :
    dias = 31
else :
    if mes in (4,5,6,9,11) :
        dias = 30
    else :
        if mes != 2 :
            print('Dato del mes incorrecto')


if mes == 2 and añoBisiesto == False :
    dias = 28
else :
    if mes == 2 :
        dias = 29


print('Este mes tiene',dias,'dias')