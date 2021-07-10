from io import open

# FUNCTIONS
def verifyFloat(dato):
    try:
        float(dato)
    except ValueError:
        return "DATO INVALIDO"
    return float(dato)

def recuperarDiaDeArchivo():
    try:
        dia = open("Quiz Archivos.txt","r")
        dia = dia.readlines()
        longdia = len(dia)
        print(dia,longdia)
        dia = dia[longdia-1].split(" ")
        dia = dia[0].split(":")
        dia = dia[1]
        return int(dia) + 1
    except FileNotFoundError:
        return 1
    

# VARIABLES
dia = 1

# EJECUCION
while True:
    print("\t\t\tPROGRAMA DE REGISTRO DE DATOS AMBIENTALES") if dia == 1 else "\n"

    minTemperatura = str(input("Ingrese la temperatura minima registrada del dia: "))
    while minTemperatura == "DATO INVALIDO":
        minTemperatura = verifyFloat(input("\tIngrese Temperatura Valida: "))
    
    maxTemperatura = str(input("Ingrese la temperatura maxima registrada del dia: "))
    while maxTemperatura == "DATO INVALIDO":
        maxTemperatura = verifyFloat(input("\tIngrese Temperatura Valida: "))

    if dia == 1:
        dia = recuperarDiaDeArchivo()
    print(dia)

    datosARegistrar = f"Dia:{dia}" + f" TemperaturaMaxima:{maxTemperatura}" + f" TemperaturaMinima:{minTemperatura}" + "\n"

    if dia == 0:
        archivoDeRegistro = open("Quiz Archivos.txt","w")
    else:
        archivoDeRegistro = open("Quiz Archivos.txt","a")
    
    archivoDeRegistro.write(datosARegistrar)

    whileBreak = str(input("Desea agregar otro registro de dia si(1) no(0): "))
    while whileBreak != "0" and whileBreak != "1":
        whileBreak = str(input("\tIngrese una opcion valida: "))
    if whileBreak == "0":
        break
    else:
        dia += 1
