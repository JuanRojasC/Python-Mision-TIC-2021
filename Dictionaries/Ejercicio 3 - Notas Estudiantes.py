# 3. crear un programa que lea (n codigos), codigo del estudiante 3 notas (1 a 5, con una cifra decimal) alumno. la primera nota corresponde 
# al 30%, la segunda al 20% .y la tercera al 50%. se debe imprimir las notas cada nota, el porcentaje. El promedio, si el alumno paso o no y 
# con que nota. y el promedio en letras con digito decimal y la nota mayor y la nota menor.

# Funciones
def printAlumno(listado):
    encabezado = ['CODIGO ESTUDIANTE', 'NOTA 1', 'NOTA 2', 'NOTA 3', 'PROMEDIO', 'ESTADO', 'NOTA MAYOR', 'NOTA MENOR']
    numeroEspacios = 13
    espacios = " " * numeroEspacios
    print(f'\n{" " * 8}{encabezado[0]}{espacios}{encabezado[1]}{espacios}{encabezado[2]}{espacios}{encabezado[3]}{espacios}{encabezado[4]}{espacios}{encabezado[5]}{espacios}{encabezado[6]}{espacios}{encabezado[7]}')
    for alumno in listado:
        columna = 0
        for valor in alumno.values():
            longitud = 0
            longitudEncabezado = 0
            for x in range(len(encabezado[columna])):
                longitudEncabezado += 1                 
            for x in range(len(str(valor))):
                longitud += 1
            
            espacios = " " * ((numeroEspacios + longitudEncabezado) - longitud)

            if valor == alumno['Codigo Estudiante']:
                print(f'{" " * 8}{valor}{espacios}',end="")

            else :
                print(f'{valor}{espacios}',end="")

            columna += 1
        print()
    print()


def PromedioLetras(numero):
    numero = str(numero)
    numero = numero.split('.')
    for i in range(len(numero)):
        if numero[i] == '0':
            letraNumero = 'cero'
        elif numero[i] == '1':
            letraNumero = 'uno'
        elif numero[i] == '2':
            letraNumero = 'dos'
        elif numero[i] == '3':
            letraNumero = 'tres'
        elif numero[i] == '4':
            letraNumero = 'cuatro'
        elif numero[i] == '5':
            letraNumero = 'cinco'
        elif numero[i] == '6':
            letraNumero = 'seis'
        elif numero[i] == '7':
            letraNumero = 'siete'
        elif numero[i] == '8':
            letraNumero = 'ocho'
        else :
            letraNumero = 'nueve'
        
        if i == 0:
            primerNumero = letraNumero
        elif i == 1:
            segundoNumero = letraNumero
    
    PromedioLetras = '{} punto {}'.format(primerNumero,segundoNumero)
    return PromedioLetras


# Variables
estado = 1
indice = 0
notaMaxima = 5
listadoEstudiantes = []

# Entradas
# Entradas
while estado == 1:
    listadoEstudiantes.append({})
    listadoEstudiantes[indice]['Codigo Estudiante'] = str(input('\nCodigo del Estudiante: '))

    for indiceNota in range(3):
        nota = round(float(input(f'Ingrese Nota {indiceNota+1}: ')),1)
        while nota < 1 or nota > 5:
            nota = round(float(input(f'\tIngrese Nota {indiceNota} Valida: ')),1)
        listadoEstudiantes[indice][f'Nota {indiceNota+1}'] = nota

    listadoEstudiantes[indice]['Promedio'] = ((((listadoEstudiantes[indice]['Nota 1'] / notaMaxima) * 0.3)
                                             + ((listadoEstudiantes[indice]['Nota 2'] / notaMaxima) * 0.2) 
                                             + ((listadoEstudiantes[indice]['Nota 3'] / notaMaxima) * 0.5))
                                             * 5)


    if listadoEstudiantes[indice]['Promedio'] >= 3:
        listadoEstudiantes[indice]['Estado'] = 'APROBADO'
    else:
        listadoEstudiantes[indice]['Estado'] = 'REPROBADO'

    listadoEstudiantes[indice]['Nota Mayor'] = listadoEstudiantes[indice]['Nota 1']
    if listadoEstudiantes[indice]['Nota 2'] > listadoEstudiantes[indice]['Nota Mayor']:
        listadoEstudiantes[indice]['Nota Mayor'] = listadoEstudiantes[indice]['Nota 2']
    if listadoEstudiantes[indice]['Nota 3'] > listadoEstudiantes[indice]['Nota Mayor']:
        listadoEstudiantes[indice]['Nota Mayor'] = listadoEstudiantes[indice]['Nota 3']

    listadoEstudiantes[indice]['Nota Menor'] = listadoEstudiantes[indice]['Nota 1']
    if listadoEstudiantes[indice]['Nota 2'] < listadoEstudiantes[indice]['Nota Menor']:
        listadoEstudiantes[indice]['Nota Menor'] = listadoEstudiantes[indice]['Nota 2']
    if listadoEstudiantes[indice]['Nota 3'] < listadoEstudiantes[indice]['Nota Menor']:
        listadoEstudiantes[indice]['Nota Menor'] = listadoEstudiantes[indice]['Nota 3']
    
    estado = int(input('\nDesea añadir otro alumno si(1) no(0): '))
    while estado != 1 and estado != 0:
        estado = int(input('\t<ERROR> Ingrese una opcion valida: '))

    indice += 1


print(listadoEstudiantes)
print(PromedioLetras(listadoEstudiantes[0]['Promedio']))
printAlumno(listadoEstudiantes)