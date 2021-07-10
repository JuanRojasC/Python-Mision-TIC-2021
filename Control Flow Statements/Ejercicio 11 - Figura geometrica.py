# Entrada de datos 
lado1 = int(input('Ingrese la medida del primer lado: '))
lado2 = int(input('Ingrese la medida del segundo lado: '))
lado3 = int(input('Ingrese la medida del tercer lado: '))
lado4 = int(input('Ingrese la medida del cuarto lado: '))


# Comprobacion
if lado1 == lado2 and lado1 == lado3 and lado1 == lado4 :
    print('La figura es un cuadrado')
else :
    if (lado1 == lado2 or lado1 == lado3 or lado1 == lado4) and (lado1 != lado2 or lado1 != lado3 or lado1 != lado4):
        print('La figura es un rectangulo')
    else :
        print('La figura no es un cuadrado o un rectangulo')


