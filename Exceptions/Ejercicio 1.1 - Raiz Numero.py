# Funciones
def raizNumero(numero):
    # Verifica si el numero es negativo
    if numero[0] == '-':
        return 'No se puede hallar la raiz de un numero negativo'

    # Verifica si se puede hallar la raiz del numero
    try:
        pow(float(numero),0.5)
    except ValueError:
        # Cambia la Descripcion del Error (Bloquea Programa)
        raise TypeError ('ERROR <<No se ha podido hallar la raiz cuadrada del dato ingresado>>')
    return pow(float(numero),0.5)

# Entradas
numeroIngresado = input('Ingrese un numero >>> ')

# Salidas
print(raizNumero(numeroIngresado))  