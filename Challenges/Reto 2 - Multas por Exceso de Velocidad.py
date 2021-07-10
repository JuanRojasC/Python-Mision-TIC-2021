# Entradas
distancia, velocidadMaxima, tiempo = input().split()


# Variables
distancia = float(distancia)
velocidadMaxima = float(velocidadMaxima) * 1000 #metros
tiempo = float(tiempo)

# Operaciones
velocidadMedia = (distancia / tiempo) * 3600 #segundos

if velocidadMaxima <= 0 or distancia <= 0 or tiempo <= 0:
    print('MEDICION ERRONEA')
    
elif velocidadMedia <= velocidadMaxima :
    print('OK')

elif velocidadMaxima < velocidadMedia <= (velocidadMaxima * 1.15) :
    print('MULTA')

elif velocidadMedia > (velocidadMaxima * 1.15) :
    print('CURSO SENSIBILIZACION')

