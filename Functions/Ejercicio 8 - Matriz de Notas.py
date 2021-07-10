# * crear un programa que lea 5 nombres de alumnos, cada alumno tiene 5 notas
# por materia ( las 5 notas se almacenan en una matriz( y el promedio de las notas
# se almacenan al final de la matriz en la misma fila, se deve:
# 1)inicializar el arreglo con los nombres de alumnos
# 2) un arreglocon los nombres de las materias
# 3) y la matriz con las notas de los alumnos de cada materia.cada fila de la matriz
# representa las notas de un alumno con su respectiva materia
# se imprime la mayor nota por materia, el promedio, la menor nota, la mayor nota
# de todos los alumnos y la menor, la cantidad de notas repetidas, la cantidad de notas
# menores a 3 y a que materia pertenece
# imprimir el prmedio en letras y numeros por cada alumno y si paso o no. Y promedio general en letras y numeros

# Variables
estado = 1
indiceFila = 1
materias = ['Matematicas', 'Sociales', 'Ciencias Naturales', 'Informatica', 'Lenguaje']
matrizNotas = [[0 for j in range (8)] for i in range (6)]
matrizNotas[0] = ['ALUMNO', 'MATERIA', 'NOTA 1', 'NOTA 2', 'NOTA 3', 'NOTA 4', 'NOTA 5', 'PROMEDIO']


# Entradas
while estado == 1:
    promedio = 0

    for x in range(0,len(matrizNotas[0])):
        if x == 0:
            alumno = str(input('\nNombre del alumno: '))
            matrizNotas[indiceFila][x] = alumno

        elif x == 1:
            materia = int(input('Seleccione la asignatura:\n\tMatematicas(1) - Sociales(2) - Ciencias Naturales(3) - Informatica(4) - Lenguaje(5) >> '))
            materia = materias[materia-1]
            matrizNotas[indiceFila][x] = materia

        elif x == (len(matrizNotas[0]) - 1):
            for y in range(2,len(matrizNotas[0]) - 1):
                promedio += matrizNotas[indiceFila][y]
                if y == len(matrizNotas[0]) - 2:
                    matrizNotas[indiceFila][y+1] = round(promedio / y, 1)

        else :
            nota = float(input('Ingrese la nota {}: '.format(x-1)))
            matrizNotas[indiceFila][x] = nota

    if indiceFila == 5:
        estado = 0
    else :
        estado = int(input('\nDesea agregar otro alumno si(1) no(0): '))
        while estado != 1 and estado != 0:
            estado = int(input('\t<ERROR> Ingrese una opcion valida: '))
        indiceFila += 1
    


# Salida
for y in range (len(matrizNotas)):
    if matrizNotas[y][0] == 0:
        break

    else :
        longitudNombreEstudiante = 0
        longitudNombreMateria = 0
        for x in range (len(matrizNotas[y][0])):
            longitudNombreEstudiante += 1
        espacioNombre = 32 - longitudNombreEstudiante

        for x in range (len(matrizNotas[y][1])):
            longitudNombreMateria += 1
        espacioMateria = 25 - longitudNombreMateria

        if y == 0:
            espacios = 12
            encabezado = 2
            espacioEspecial = 18
        else :
            espacios = 15
            espacioEspecial = espacios + 8
            espacioMateria += 1
        
        print(" " * encabezado, matrizNotas[y][0],end="")
        print(" " * espacioNombre, matrizNotas[y][1],end="")
        print(" " * espacioMateria, matrizNotas[y][2],end="")
        print(" " * espacios, matrizNotas[y][3],end="")
        print(" " * espacios, matrizNotas[y][4],end="")
        print(" " * espacios, matrizNotas[y][5],end="")
        print(" " * espacios, matrizNotas[y][6],end="")
        print(" " * espacioEspecial, matrizNotas[y][7])


print('\n')


        
