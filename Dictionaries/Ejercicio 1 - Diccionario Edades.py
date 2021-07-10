# 1. Crear un programa en python que lea (n datos), el nombre, el año de nacimiento y el año actual de dos 
# personas. Se debe mostrar el nombre y la edad de cada una de las personas en años, meses, días , minutos 
# y segundos y el promedio de edades en años. Todos los meses son de 30 días.

# Funciones
def printDato(diccionario):
    global indice
    suma = 0
    for llave, valor in diccionario.items():
        print(f'\n{llave}\nEdad en años: {valor[2]}\nEdad en meses: {valor[3]}\nEdad en dias: {valor[4]}\nEdad en minutos: {valor[5]}\nEdad en segundos: {valor[6]}\n')
        suma += valor[2]
    print(suma/indice)

# Entradas
estado = 1
indice = 0
datosPersonas = {}

while estado == 1:
    Nombre = str(input('\nNombre de la persona: ')).upper()
    datosPersonas[Nombre] = [(int(input('Año de nacimiento: ')))]
    datosPersonas[Nombre].append(int(input('Año actual: ')))
    datosPersonas[Nombre].append(datosPersonas[Nombre][1] - datosPersonas[Nombre][0])
    datosPersonas[Nombre].append(datosPersonas[Nombre][2] * 12)
    datosPersonas[Nombre].append(datosPersonas[Nombre][3] * 30)
    datosPersonas[Nombre].append(datosPersonas[Nombre][3] * (60*24))
    datosPersonas[Nombre].append(datosPersonas[Nombre][4] * 3600)
    
    estado = int(input('\nDesea agregar otra persona si(1) no(0): '))
    while estado != 1 and estado != 0:
        estado = int(input('\t<ERROR> Ingrese una opcion valida: '))
    
    indice += 1

printDato(datosPersonas)

