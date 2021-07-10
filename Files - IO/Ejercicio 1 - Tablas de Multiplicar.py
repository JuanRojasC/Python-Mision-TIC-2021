from io import open
# Numeros Pedidos entre 1 y 20 y las tablas de multiplicar de los que estan entre 8 y 11

# VARIABLES
inputNumbers = []
strInputNumbers = ""

# EXECUTION
while True:
    # REQUEST A NUMBER BETWEEN 1 AND 20
    inputNumber = int(input("Ingrese un numero entre 1 - 20: "))
    while inputNumber < 1 or inputNumber > 20:
        inputNumber = int(input("\n\tIngrese un numero valido: "))

    # ADD NUMBER TO A LIST
    inputNumbers.append(str(inputNumber))
    # ADD NUMBER TO A STRING
    strInputNumbers = ','.join(inputNumbers) 

    # ASK FOR CONTINUOS ENTRY NUMBERS
    whileBreak = input("Desea agregar otro numero si(1) no(0): ")
    while whileBreak != "0" and whileBreak != "1":
        whileBreak = str(input("\n\tIngrese una opcion valida: "))
    if whileBreak == "0":
        break

# CREATE FILE
fileNumbers = open("Desarrollo Ejercicio 1.txt","w")
fileNumbers.write(strInputNumbers)
fileNumbers.close