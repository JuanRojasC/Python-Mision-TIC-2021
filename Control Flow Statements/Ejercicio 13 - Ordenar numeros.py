# Entradas
numero1 = int(input('Ingrese el primer numero: '))
numero2 = int(input('Ingrese el segundo numero: '))
numero3 = int(input('Ingrese el tercer numero: '))

# Organizar
if numero1 == numero2 and numero2 == numero3 :
    print(numero1,numero2,numero3)
    
if numero1 > numero2 and numero2 > numero3 :
    print(numero3,numero2,numero1)
    
if numero1 > numero2 and numero3 > numero2 and numero1 > numero3 :
    print(numero2,numero3,numero1)
    
if numero1 > numero2 and numero3 > numero2 and numero3 > numero1 :
    print(numero2,numero1,numero3)
    
if numero2 > numero1 and numero3 > numero2:
    print(numero1,numero2,numero3)
    
if numero2 > numero1 and numero3 < numero1:
    print(numero3,numero1,numero2)
    
if numero2 > numero1 and numero3 < numero2 and numero3 > numero1 :
    print(numero1,numero3,numero2)