sueldo = float(input('Ingrese el monto de su salario: '))

if sueldo >= 1000000 :
    sueldo = sueldo * 1.12
if sueldo < 1000000 :
    sueldo = sueldo * 1.15


print(round(sueldo))
