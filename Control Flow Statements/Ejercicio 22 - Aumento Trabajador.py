# 13  Construya un programa  tal que dado como datos la categoría y el sueldo de un trabajador, calcule el aumento correspondiente 
#     teniendo en cuenta la siguiente tabla. Imprima la categoría del trabajador y su nuevo sueldo:
#    CATEGORIA	AUMENTO
#    1	15%
#    2	10%
#    3	8%
#    4	7%

sueldoTrabajador = int(input('Ingrese el salario del trabajador: '))
categoriaTrabajor = int(input('Ingrese la categoria del trabajador: '))

if categoriaTrabajor == 1 :
    sueldoTrabajador = sueldoTrabajador * 1.15
if categoriaTrabajor == 2 :
    sueldoTrabajador = sueldoTrabajador * 1.1
if categoriaTrabajor == 3 :
    sueldoTrabajador = sueldoTrabajador * 1.08
if categoriaTrabajor == 4 :
    sueldoTrabajador = sueldoTrabajador * 1.04

print('El nuevo salario del trabajador es: ',sueldoTrabajador)