# 4 Construya un programa que permita (n nombres) leer nombre,  salario y número de hijos de un empleado, calcular subsidio de transporte, 
# subsidio familiar, valor de aporte salud,  valor de aporte pensión y total a pagar. Mediante un mensaje mostrar nombre, subsidio de transporte, 
# subsidio familiar, valor de aporte salud, valor de aporte pensión y total a pagar.

# Funciones

def totalSueldo(lista):
    indice = lista
    sueldoTotal = 0
    for llave, valor in indice.items():
        if type(valor) == int or type(valor) == float:
            if llave == 'Salario' or llave == 'Subsidio Transporte' or llave == 'Subsidio Familiar':
                sueldoTotal += valor
            elif llave != 'Total Aportes':
                sueldoTotal -= valor 
    
    return sueldoTotal

def printEmpleado(lista):
    encabezado = ['EMPLEADO','SUELDO','NRO HIJOS','SUBSIDIO TRANSPORTE','SUBSIDIO FAMILIAR','APORTE SALUD','APORTE PENSION','TOTAL APORTES','TOTAL SUELDO']
    numeroEspacios = 8
    espacios = " " * numeroEspacios
    for columna in range(len(encabezado)):
        if columna == 0:
            print(f'{" " * 2}{encabezado[columna]}{" " * 6}',end="")
        else:
            print(f'{espacios}{encabezado[columna]}',end="")
    
    for empleado in lista:
        columna = 0
        for dato in empleado.values():
            longitudEncabezado = 0
            longitudDato = 0
            for long in range(len(encabezado[columna])):
                longitudEncabezado += 1
            for long in range(len(str(dato))):
                longitudDato += 1
            espacios = " " * ((longitudEncabezado + numeroEspacios) - longitudDato)

            if dato == empleado['Nombre']:
                print(f'{" " * 2}{dato}{" " * ((longitudEncabezado + 14) - longitudDato)}',end="")
            elif dato == empleado['Sueldo Final']:
                print(f'{dato}')
            else:
                print(f'{dato}{espacios}',end="")
            
            columna += 1



# Variables
estado = 1
indice = 0
salarioMinimo = 908526
subsidioFamiliar = 40000
listadoEmpleados = []


# Entradas
while estado == 1:

    listadoEmpleados.append({})
    listadoEmpleados[indice]['Nombre'] = str(input('\nNombre del Empleado: '))
    listadoEmpleados[indice]['Salario'] = float(input('Salario: '))
    listadoEmpleados[indice]['Numero Hijos'] = int(input('Numero de Hijos: '))

    # Subsidio De Transporte
    if listadoEmpleados[indice]['Salario'] <= (salarioMinimo*2) :
        listadoEmpleados[indice]['Subsidio Transporte'] = 106454
    else:
        listadoEmpleados[indice]['Subsidio Transporte'] = 'No Aplica'
        
    # Subsidio Familiar   
    if listadoEmpleados[indice]['Salario'] <= (salarioMinimo*4) :
        listadoEmpleados[indice]['Subsidio Familiar'] = subsidioFamiliar * listadoEmpleados[indice]['Numero Hijos']
    else :
        listadoEmpleados[indice]['Subsidio Familiar'] = 'No Aplica'

    # Aporte Salud
    listadoEmpleados[indice]['Aporte Salud'] = round((listadoEmpleados[indice]['Salario']/100) * 4)

    # Aporte Pension
    listadoEmpleados[indice]['Aporte Pension'] = round((listadoEmpleados[indice]['Salario']/100) * 4)

    # Total Aportes
    listadoEmpleados[indice]['Total Aportes'] = listadoEmpleados[indice]['Aporte Salud'] + listadoEmpleados[indice]['Aporte Pension']

    # Sueldo Despues de Aportes
    listadoEmpleados[indice]['Sueldo Final'] = totalSueldo(listadoEmpleados[indice]) 
    

    estado = int(input('\nDesea añadir otro alumno si(1) no(0): '))
    while estado != 1 and estado != 0:
        estado = int(input('\t<ERROR> Ingrese una opcion valida: '))

    indice += 1

printEmpleado(listadoEmpleados)