# craer un programa que almacene en una lista el nombre del producto, cantidad, vlr unitario, descuento hacerlo para 3 productos.
#   ejemplo tienda=["pantalones",2,30000,10,tapabocas,10,5000,5,alcohol,3,10000,2]. e inserte despues de los datos de cada producto, 
#   el valor del iva valor descuento y el valor total a pagar. El imprima cada producto, (nombre del producto  cantidad, vlr unitario, 
#   vlr iva, vlr del descuento y valor total a pagar)

# Datos
productos = ['computador hp',23,1063500,'computador asus',15,2155000,'computador lenovo',10,1880000]

indice = 0

# Funciones
def añadirDato(valor,producto,array):
    indice = array.index(producto)
    if (len(array) - indice) > 5:
        for x in range (indice+1,len(array)):
            if type(array[x]) == str:
                array.insert(x,valor)
                return False
    else:
        array.append(valor)





# Entradas
numeroProductos = 0
for x in range(len(productos)):
    if type(productos[x]) == str:
        numeroProductos += 1
numeroProductos = numeroProductos *2

for x in range (len(productos)+numeroProductos):
    if type(productos[x]) == str:
        producto = productos[x]
        print('\nProducto << {} >>'.format(productos[x]))

        IVA = float(input('Ingrese el porcentaje del IVA: '))
        añadirDato(IVA,producto,productos)

        Descuento = float(input('Ingrese el porcentaje de descuento: '))
        añadirDato(Descuento,producto,productos)

        Total = (productos[x+2] * ((IVA/100) + 1)) * ((100-Descuento)/100)
        añadirDato(Total,producto,productos)




# Salidas
for x in range(len(productos)):
    if type(productos[x]) == str:
        print('\nProducto:',productos[x])
        print('Stock:',productos[x+1])
        print('Valor Unitario:',productos[x+2])
        print('IVA:',productos[x+3],'%')
        print('Descuento:',productos[x+4],'%')
        print('Total:',productos[x+5])



