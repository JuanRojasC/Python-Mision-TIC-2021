# 2.Crear un programa en python que lea el nombre del producto, cantidad del producto, vlr unitario
# si el subtota(cantidad * vlr) si es maypr a $10000 se le realizara un descuento del 15%
# si no el descuento es 5%. mostrar nombre del producto, cantidad, vrl unitario, valor a pagar, iva 19&
# porcentaje del descuento, valor del descuento y valor total a pagar. 

# Entrada de datos
nombreProducto = str(input('Ingese el nombre del producto: '))
cantidadProducto = float(input('Ingrese la cantidad de producto: '))
valorUnitario = float(input('Ingrese el valor unitario del porducto: '))

# Calculos
iva = 19
subtotal = cantidadProducto * valorUnitario

if subtotal > 10000 :
    subtotal = subtotal * 0.85
else :
    subtotal = subtotal * 0.95

total = subtotal * ((iva/100) + 1)

# Impresion
print('\nProducto: {}\nCantidad: {}\nSubtotal: {}\nIVA: {}\nTotal: {}\n'.format(nombreProducto,cantidadProducto,subtotal,iva,total))