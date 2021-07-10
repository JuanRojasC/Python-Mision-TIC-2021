def verificarOp(opcion):
    try:
        opcion = int(opcion)
    except ValueError:
        opcion = 'ERROR'
    return opcion

def verificarString(dato):
    try:
        dato = str(dato)
    except ValueError:
        dato = 'ERROR'
    return dato

def verificarFloat(dato):
    try:
        dato = float(dato)
    except ValueError:
        dato = 'ERROR'
    return dato


numero = 13.355
print(int(numero))

op=0
while op != 4: 
    print("\n\t MENU")
    print("\t 1. CADENA")
    print("\t 2. SUELDO")
    print("\t 3. NOTA") 
    print("\t 4. SALIR")

    op='ERROR'
    while op == 'ERROR':
        op = verificarOp(input("\n\t Elija una de las opciones >>> "))

    if op ==1:
        cadena='ERROR'
        while cadena == 'ERROR':
            cadena = verificarString(input( "palabra  "))
        vocal='ERROR'
        while vocal == 'ERROR':
            vocal=input(" letra  ")
        cane=0
        x=0
        for x in range (len(cadena)):
            if cadena[x] == vocal:
                cane=cane+1
        print ( "la letra ",vocal ,"esta ",cane, " veces en " , cadena) 

    if op == 2:
        can = 'ERROR'
        while can == 'ERROR' or can == 0:
            can = verificarOp(input(" \n ingrese cantidad de sueldos: "))
        sumat=0
        cont=0
        sumav=0
        for x in range (1,can+1):
            can = 'ERROR'
            while can == 'ERROR':
                can=verificarFloat(input(" sueldo "))
            if can >= 1000000 and can < 1500000:
                sumav= sumav + can
                cont = cont+1 
            sumat = sumat + can
        print("\n \t La sumatoria del rango es ", sumav, " y el promedio " ,round(sumav/cont) if sumav > 0 else '0')
        print(" \t La sumatoria total de sueldos es :", sumat)

    if op == 3:
        x = 0
        suma = 0
        mayor = 0
        menor = 0
        sumat=0
        nota = 'ERROR'
        while nota == 'ERROR':
            nota = verificarOp(input(" \n ingrese cantidad de notas: "))
        canti=0
        for i in range (1,nota+1):
            nota=0
            while nota < 1 or nota > 5:
                nota = 'ERROR'
                while nota == 'ERROR':
                    nota = verificarFloat(input(" \n \t ingrese nota de 1 a 5 "))
                if nota < 1 or nota > 5:
                    print(" la nota debe estar ente 1 y 5  ")
            canti = canti + 1 
            suma = suma + nota
            x=x+1
            if nota > mayor:
                 mayor = nota
            if nota < menor:
                menor = nota
        prom=suma/canti
        
        print(" \n La sumatoria de notaas es: {} la nota mayor es: {} la nota menor es: {} el promedio es: {:.1f}".format(suma,mayor,menor,prom))

    if op == 4:
        quit


