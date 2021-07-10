# 2. Crear un programa en python que lea (para n productos) el nombre del producto, cantidad del producto, vlr unitario
# si el subtota(cantidad * vlr) si es maypr a $10000 se le realizara un descuento del 15%
# si no el descuento es 5%. mostrar nombre del producto, cantidad, vrl unitario, valor a pagar, iva 19&
# porcentaje del descuento, valor del descuento y valor total a pagar.

# Funciones
def printProducto(listado):
    encabezado = ['Producto', 'Cantidad', 'Vlr Unitario', 'Subtotal', 'Descuento', 'IVA', 'Total']
    numeroEspacios = 13
    espacios = " " * numeroEspacios
    print(f'\n{" " * 8}{encabezado[0]}{espacios}{encabezado[1]}{espacios}{encabezado[2]}{espacios}{encabezado[3]}{espacios}{encabezado[4]}{espacios}{encabezado[5]}{espacios}{encabezado[6]}')
    for producto in listado:
        columna = 0
        for valor in producto.values():
            longitudEncabezado = 0
            for x in range(len(encabezado[columna])):
                longitudEncabezado += 1
            longitud = 0
            if type(valor) == str:
                for x in range(len(valor)):
                    longitud += 1
                espacios = " " * ((numeroEspacios + 8) - longitud)
                print(f'{" " * 8}{valor}{espacios}',end="")
            else :
                for x in range(len(str(valor))):
                    longitud += 1
                espacios = " " * ((numeroEspacios + longitudEncabezado) - longitud)
                print(f'{valor}{espacios}',end="")

            columna += 1
        print()
    print()


# Variables
estado = 1
indice = 0
iva = 0.19
listadoProductos = []

# Entradas
while estado == 1:
    listadoProductos.append({})
    listadoProductos[indice]['Producto'] = str(input('\nNombre del producto: '))
    listadoProductos[indice]['Cantidad'] = float(input('Cantidad de producto: '))
    listadoProductos[indice]['Valor Unitario'] = float(input('Valor Unitario: '))

    
    listadoProductos[indice]['Subtotal'] = listadoProductos[indice]['Cantidad'] * listadoProductos[indice]['Valor Unitario']
    if listadoProductos[indice]['Subtotal'] > 10000:
        listadoProductos[indice]['Descuento'] = 15/100
    else :
        listadoProductos[indice]['Descuento'] = 5/100

    listadoProductos[indice]['IVA'] = iva

    listadoProductos[indice]['Total'] = ((listadoProductos[indice]['Subtotal'] 
                                            * (1 - listadoProductos[indice]['Descuento']))
                                            * (listadoProductos[indice]['IVA'] + 1))

    
    estado = int(input('\nDesea añadir otro producto si(1) no(0): '))
    while estado != 1 and estado != 0:
        estado = int(input('\t<ERROR> Ingrese una opcion valida: '))

    indice += 1

printProducto(listadoProductos)