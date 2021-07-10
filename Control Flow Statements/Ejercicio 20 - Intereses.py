cantidad = int(input('Cantiad a prestar: '))
intereses = float(input('Interes diario: '))
duracion = int(input('Dias de prestamo: '))

interesProducido = (cantidad*intereses*duracion)/(360*100)

if interesProducido > (cantidad/100) * 30 :
    print('El prestamo no se solicitara')
if interesProducido < (cantidad/100) * 30 :
    print ('El prestamo se solicitara')
 