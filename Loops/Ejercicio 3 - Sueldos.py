# 3  Crear un programa que lea n sueldos y muestre los sueldos sumatoria y promedio de los sueldos leidos(los sueldos leidos deben estre el minimo y 2000000)
#    de los sueldos leidos mayores del minimo y menores de $1500000

estado = 1
sumatoria = 0
promedio = 0
numeroCola = 0


while estado == 1 :
    sueldo = float(input('Ingrese el valor de un sueldo (908000 hasta 2000000): '))
    while  sueldo < 908000 or sueldo > 2000000 :
        sueldo = float(input('<ERROR> el valor ingresado no cumple los limites\nIngrese el valor de un sueldo: '))
    numeroCola += 1
    if  908000 <= sueldo <= 1500000 :
        sumatoria += sueldo
        promedio = sumatoria / numeroCola
    estado = int(input('Desea ingresar otro sueldo si(1) no(0): '))

print('La sumatoria de todos los sueldos mayores a 908000 y menores a 1500000 es de {}'.format(sumatoria))
print('El promedio de todos los sueldos mayores a 908000 y menores a 1500000 es de {:.1f}'.format(promedio))