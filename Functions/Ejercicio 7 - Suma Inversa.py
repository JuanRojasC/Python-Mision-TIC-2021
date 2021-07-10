# crea un programa  dos vectores de igual tamaño y cree un nuevo vector con la suma del primer elemento de la lista1 con el ultimo elemnto de
# de la lista 2 y asi sucesicamente

# Variables
vector1 = [0,1,2,3,4,5,6,7,8,9]
vector2 = [9,8,7,6,5,4,3,2,1,0]

vectorResultante =  vector1


# Operacion
for i, j in zip(range(len(vector1)), range((len(vector2) - 1), -1, -1)):
    vectorResultante[i] = vector1[i] + vector2[j]


# Salida
print(vectorResultante)
