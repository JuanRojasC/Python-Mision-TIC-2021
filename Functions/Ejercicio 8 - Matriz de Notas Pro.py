# * crear un programa que lea 5 nombres de alumnos, cada alumno tiene 5 notas
# por materia ( las 5 notas se almacenan en una matriz( alumno el promedio de las notas
# se almacenan al final de la matriz en la misma fila, se deve:
# 1)inicializar el arreglo con los nombres de alumnos
# 2) un arreglocon los nombres de las materias
# 3) alumno la matriz con las notas de los alumnos de cada materia.cada fila de la matriz
# representa las notas de un alumno con su respectiva materia
# se imprime la mayor nota por materia, el promedio, la menor nota, la mayor nota
# de todos los alumnos alumno la menor, la cantidad de notas repetidas, la cantidad de notas
# menores a 3 alumno a que materia pertenece
# imprimir el prmedio en letras alumno numeros por cada alumno alumno si paso o no. Y promedio general en letras alumno numeros


# Variables
estado = 1
indiceEstudiante = 1
materias = ['Matematicas', 'Sociales', 'Ciencias Naturales', 'Informatica', 'Lenguaje']
matrizNotas = [[[0 for i in range (7)] for j in range (6)] for j in range(6)]
matrizNotas[0] = ['ALUMNO', 'MATERIA', 'NOTA 1', 'NOTA 2', 'NOTA 3', 'NOTA 4', 'NOTA 5', 'PROMEDIO']
print(matrizNotas)

# Funciones
def printMatriz(list):
    for x in range(len(list)):
        if x == 0:
            print('\n', list[x])
        else :
            for alumno in range(len(list[x])):
                print(list[x][alumno],'\n')


# Entradas
while estado == 1:
    for alumno in range(1,len(matrizNotas)):

        for asignatura in range(0,len(matrizNotas)-1):

            # Definicion de Alumno
            nombreAlumno = str(input('Nombre del Alumno: ')).lower()
            alumnoExistente = False
            indicesVacios = 0
            for fila in range(1,len(matrizNotas)):
                if nombreAlumno in matrizNotas[fila]:
                    alumno = fila
                    alumnoExistente = True
                    break
            if alumnoExistente == False:
                for fila in range(1,len(matrizNotas)):
                    if matrizNotas[fila][0][0] == 0:
                        matrizNotas[fila][0] = nombreAlumno
                        alumno = fila
                        break
            

            # Definicion de Materia
            materia = int(input('Seleccione la asignatura:\n\tMatematicas(1) - Sociales(2) - Ciencias Naturales(3) - Informatica(4) - Lenguaje(5) >> '))
            materia = materias[materia - 1]
            materiaExistente = False
            for fila in range(1,len(matrizNotas[alumno])):
                if materia in matrizNotas[fila]:
                    materia = fila
                    materiaExistente = True
                    break
            
            if materiaExistente == False:
                for fila in range(1,len(matrizNotas[alumno])):  
                    if matrizNotas[alumno][fila][0] == 0:
                        matrizNotas[alumno][fila][0] = materia
                        materia = fila
                        break
                

            # Entrada de notas
            for indiceNota in range(1,len(matrizNotas[alumno][materia])):
                promedio = 0
                if indiceNota == (len(matrizNotas[alumno][materia]) - 1):
                    for nota in range(1,len(matrizNotas[alumno][materia]) - 1):
                        promedio += matrizNotas[alumno][materia][nota]
                        if nota == len(matrizNotas[alumno][materia]) - 2:
                            matrizNotas[alumno][materia][nota+1] = round(promedio / nota, 1)
                else:
                    nota = float(input('Ingrese la nota {}: '.format(indiceNota)))
                    matrizNotas[alumno][materia][indiceNota] = nota

            # Agregar mas alumnos
            estado = int(input('\nDesea añadir otro alumno o modificar sus notas si(1) no(0): '))
            while estado != 1 and estado != 0:
                estado = int(input('\t<ERROR> Ingrese una opcion valida: '))
            if estado == 0:
                break
        
        if estado == 0:
            break
                
            print('\n')
        


# Salida
for alumno in range(len(matrizNotas)):
    if matrizNotas[alumno][0] == 0:
        break

    elif alumno == 0:
        espacios = 12
        encabezado = 2
        espacioNombre = 32 - 6
        espacioEspecial = 18
        espacioMateria = 25 - 7
        print(" " * encabezado, matrizNotas[alumno][0],end="")
        print(" " * espacioNombre, matrizNotas[alumno][1],end="")
        print(" " * espacioMateria, matrizNotas[alumno][2],end="")
        print(" " * espacios, matrizNotas[alumno][3],end="")
        print(" " * espacios, matrizNotas[alumno][4],end="")
        print(" " * espacios, matrizNotas[alumno][5],end="")
        print(" " * espacios, matrizNotas[alumno][6],end="")
        print(" " * espacioEspecial, matrizNotas[alumno][7])

    else :
        for materia in range(1,len(matrizNotas[alumno])):
            if matrizNotas[alumno][materia][0] == 0:
                break

            else :
                longitudNombreEstudiante = 0
                longitudNombreMateria = 0
                for x in range (len(matrizNotas[alumno][0])):
                    longitudNombreEstudiante += 1
                espacioNombre = 32 - longitudNombreEstudiante

                for x in range (len(matrizNotas[alumno][materia][0])):
                    longitudNombreMateria += 1
                espacioMateria = 25 - longitudNombreMateria
                
                espacios = 15
                espacioEspecial = espacios + 8
                espacioMateria += 1
                
                if materia == 1:
                    print()
                    print(" " * encabezado, matrizNotas[alumno][0],end="")
                    print(" " * espacioNombre, matrizNotas[alumno][materia][0],end="")
                    print(" " * espacioMateria, matrizNotas[alumno][materia][1],end="")
                    print(" " * espacios, matrizNotas[alumno][materia][2],end="")
                    print(" " * espacios, matrizNotas[alumno][materia][3],end="")
                    print(" " * espacios, matrizNotas[alumno][materia][4],end="")
                    print(" " * espacios, matrizNotas[alumno][materia][5],end="")
                    print(" " * espacioEspecial, matrizNotas[alumno][materia][6])

                else :
                    print(" " * (encabezado + longitudNombreEstudiante),end=" ")
                    print(" " * espacioNombre, matrizNotas[alumno][materia][0],end="")
                    print(" " * espacioMateria, matrizNotas[alumno][materia][1],end="")
                    print(" " * espacios, matrizNotas[alumno][materia][2],end="")
                    print(" " * espacios, matrizNotas[alumno][materia][3],end="")
                    print(" " * espacios, matrizNotas[alumno][materia][4],end="")
                    print(" " * espacios, matrizNotas[alumno][materia][5],end="")
                    print(" " * espacioEspecial, matrizNotas[alumno][materia][6])


print('\n')
        
