# 8. Leer un numero entre la edad de una persona y mostrar si es Bebe, si es niño, si es joven,  si adulto joven, adulto maduro o adulto mayor.

# Entrada
age = int(input('Ingrese su edad: '))

# Compracion
if age < 2 :
    print('El individuo es un bebe')
else :
    if age < 10 :
        print('El indivudo es un niño')
    if 10 <= age < 21 :
        print('El individuo es un joven')
    if 21 <= age < 35 :
        print('El indivudo es un adulto joven')
    if 35 <= age < 49 :
        print('El individuo es un adulto maduro')
    if age > 49 :
        print('El indivuo es un adulto mayor')