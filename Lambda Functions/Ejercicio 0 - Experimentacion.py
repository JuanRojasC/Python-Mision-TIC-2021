# FUNCIONES LAMBDA O ANONIMAS

funcion = lambda parametro : parametro
funcionSuma = lambda parametro1,parametro2 : parametro1 + parametro2
funcionResta = lambda parametro1,parametro2 : parametro1 - parametro2
funcionMultiplicacion = lambda parametro1,parametro2 : parametro1 * parametro2
funcionDivision = lambda parametro1,parametro2 : parametro1 / parametro2
funcionModulo = lambda parametro1,parametro2 : parametro1 % parametro2

print(funcion(5))
print(funcionSuma(5,5))
print(funcionResta(5,5))
print(funcionMultiplicacion(5,5))
print(funcionDivision(5,5))
print(funcionModulo(5,5))

# METODOS DE ARRAYS (filter-map)
numeros = '123456789'

# METODO FILTER
numerosImpares = list(filter(lambda elemento: (int(elemento) % 2 == 1), numeros))
print(numerosImpares)


# METODO MAP
numerosPotencia = list(map(lambda numero: int(numero) ** 2, numeros))
print(numerosPotencia)

