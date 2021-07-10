# 1  Crear un programa que lea n cantidad de numeros y muestre la sumatoria y prommedio de los numeros
estado = 1
sumatoria = 0
promedio = 0
numeroCola = 0

while estado == 1 :
    numero = int(input('Ingrese un numero: '))
    numeroCola += 1
    sumatoria += numero
    promedio = sumatoria / numeroCola
    estado = int(input('Desea ingresar otro numero si(1) no(0): '))

print('La sumatoria de los numeros ingreados es {}\nEl promedio de los numero ingresados es {}'.format(sumatoria,promedio))