# 7. Construya un programa que permita leer  la nota de un examen.  Mostrar mediante un mensaje el state del estudiante de acuerdo a la nota. 
#    NOTA	state
#    Entre 0.0 y 2.5	Deficiente
#    Entre 2.6 y 3.9	Insuficiente
#    Entre 4.0 y 4.4	Aceptable
#    Entre 4.5 y 4.9	Suficiente
#    5.0	Excelente

note1=float(input("\n ingrese nota 1 >>> "))
note2=float(input("\n ingrese nota 2 >>> "))
note3=float(input("\n ingrese nota 3 >>> "))

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


print('\n La calificacion del estudiante es', state, '\n')

# print('\n Su nota es {:0.1f}' .format(finalNote) , 'se encuentra aprobado' if finalNote>=3.5 else 'se encuentra reprobado')
