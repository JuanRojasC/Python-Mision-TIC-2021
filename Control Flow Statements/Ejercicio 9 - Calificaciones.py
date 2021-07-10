# 9.crear un programa que lea 3 notas (1 a 5, con una cifra decimal) alumno. la primera nota corresponde al 30%, la segunda al 20% .y la tercera al 50%. se debe imprimir las notas cada nota, el porcentaje. El promedio, si el alumno paso o no y con que nota. y el promedio en letras con digito decimal y la nota mayor y la nota menor.

note1=round(float(input("\n ingrese nota 1 >>> ")),1)
note2=round(float(input("\n ingrese nota 2 >>> ")),1)
note3=round(float(input("\n ingrese nota 3 >>> ")),1)

percentNote1 = (note1 / 5) * 0.3
percentNote2 = (note2 / 5) * 0.2
percentNote3 = (note3 / 5) * 0.5

finalNote = (percentNote1 + percentNote2 + percentNote3) * 5
if finalNote <= 2.5 :
    state = 'Deficiente'
elif 2.6 <= finalNote <= 3.9 :
    state = 'Insuficiente'
elif 4.0 <= finalNote <= 4.4 :
    state = 'Aceptable'
elif 4.5 <= finalNote <= 4.9 :
    state = 'Suficiente'
elif finalNote == 5 :
    state = 'Excelente'


print(' Nota\t','Porcentaje\n','Estado','')