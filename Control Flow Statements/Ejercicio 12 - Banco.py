cantidadDinero = 100000

# Tipo de Transaccion
transaccion = str(input('Desea realizar una consignacion (C) o un retiro (R): '))
if transaccion == 'C' or transaccion == 'c' :
    transaccion = 'Consignacion'
if transaccion == 'R' or transaccion == 'r':
    transaccion = 'Retiro'



# Movimiento
if transaccion == 'Consignacion' :
    cantidadDinero += int(input('Ingrese la cantidad a consginar: '))
    print('Consignacion exitosa\n','Su nuevo saldo es {}'.format(cantidadDinero))

else :
    if transaccion == 'Retiro' :
        movimiento = int(input('Ingrese la cantidad a retirar: '))
        if movimiento > cantidadDinero :
            print('Saldo en cuenta insuficiente')
        if movimiento < cantidadDinero :
            print('Retiro Exitoso\n','Su nuevo saldo es {}'.format(cantidadDinero - movimiento))

    else :
        print('Transaccion no reconocida')