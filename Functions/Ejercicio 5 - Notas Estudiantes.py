#  crear un programa con manejo de funciones que lea n notas de estudiante, las notas debe estar entre 1 y 5
#  imprimir : notas, promedio en letras y numeros, mayor nota y en que posicion entro, menor nota y en que posicion esta
#              notas en orden de la ultima a la primera, la cantidad de notas menores a 3, la catidad de notas mayores a 3,
#              cantidad de notas entre 4.5 y 5

# Entradas
notasEstudiante = []
estado = 1
indice = 1

print('\nPara salir de la entrada de notas presione (.)')

while estado == 1:
    nota = input('\nIngrese la nota {} : '.format(indice))
    if nota == '.':
        estado = 0
    else :
        nota = float(nota)
        while nota < 1 or nota > 5:
            nota = float(input('\t<ERROR Ingrese una nota valida: '))
        notasEstudiante.append(nota)
        indice += 1


# Funciones
def promedioNotas(array):
    promedio = 0
    for nota in array:
        promedio += nota
    promedio = round(promedio / len(array),1)
    return promedio

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



def notaMayor(array):
    notaMayor = array[0]
    posicionNotaMayor = 0
    for x in range(len(array)):
        if array[x] > notaMayor:
            notaMayor = array[x]
            posicionNotaMayor = x
    return (notaMayor,posicionNotaMayor)

def notaMenor(array):
    notaMenor = array[0]
    posicionNotaMenor = 0
    for x in range(len(array)):
        if array[x] < notaMenor :
            notaMenor = array[x]
            posicionNotaMenor = x
    return (notaMenor, posicionNotaMenor)


def ordenarNotas(array):
    return array.sort()


def notasReprobadas(array):
    notasReprobadas = 0
    for x in array:
        if x < 3:
            notasReprobadas += 1
    return notasReprobadas

def notasAprobadas(array):
    notasAprobadas = 0
    for x in array:
        if x >= 3:
            notasAprobadas += 1
    return notasAprobadas

def notasExcelentes(array):
    notasExcelentes = 0
    for x in array:
        if x > 4.5:
            notasExcelentes += 1
    return notasExcelentes
       

# Salidas
def impresionNotas(array):
    print('Notas: ',array)
    print('Promedio:',promedioNotas(array),'----',PromedioLetras(promedioNotas(array)))
    print('Cantidad de Notas Reprobadas:',notasReprobadas(array))
    print('Cantidad de Notas Aprobadas:',notasAprobadas(array))
    print('Cantidada de Notas Excelentes:',notasExcelentes(array))

impresionNotas(notasEstudiante)


