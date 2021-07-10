numeros = '123456789'

numerosElevados = list(map(lambda numero: int(numero) * int(numero), numeros))
print(numerosElevados)