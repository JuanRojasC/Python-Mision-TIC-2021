from io import open

diccionarioDias = []
indice = 0
diasErroneos = 0
diasErroneosMin = 0
diasErroneosMax = 0

datosArchivo = open("Quiz Archivos.txt","r")
datosArchivo = datosArchivo.readlines()
for dia in datosArchivo:
    datosDia = dia.replace("\n","").split(" ")
    datoDia = datosDia[0].split(":")
    datoMaxT = datosDia[1].split(":")
    datoMinT =datosDia[2].split(":")
    diccionarioDias.append({})
    diccionarioDias[indice]["dia"] = int(datoDia[1])
    diccionarioDias[indice]["Temperatura Minima"] = float(datoMinT[1])
    diccionarioDias[indice]["Temperatura Maxima"] = float(datoMaxT[1])
    indice += 1


# PRINT
def printDay(lista):
    global diasErroneos,diasErroneosMin,diasErroneosMax
    encabezado = ["DIA","TEMPERATURA MINIMA","TEMPERATURA MAXIMA"]
    numeroEspacios = 8
    espacios = " " * numeroEspacios
    for columna in range(len(encabezado)):
        if columna == 0:
            print(f'{" " * 2}{encabezado[columna]}{" " * 6}',end="")
        else:
            if columna == len(encabezado) - 1:
                print(f'{espacios}{encabezado[columna]}')
            else:
                print(f'{espacios}{encabezado[columna]}',end="")
    
    for day in lista:
        columna = 0
        if day["Temperatura Minima"] < 5 or day["Temperatura Maxima"] > 35:
            diasErroneos += 1
            if day["Temperatura Minima"] < 5:
                diasErroneosMin += 1
            if day["Temperatura Maxima"] > 35:
                diasErroneosMax += 1
        for dato in day.values():
            longitudEncabezado = 0
            longitudDato = 0
            for long in range(len(encabezado[columna])):
                longitudEncabezado += 1
            for long in range(len(str(dato))):
                longitudDato += 1
            espacios = " " * ((longitudEncabezado + numeroEspacios) - longitudDato)
            
            if dato == day['dia']:
                print(f'{" " * 2}{dato}{" " * ((longitudEncabezado + 14) - longitudDato)}',end="")
            else:
                if dato == day["Temperatura Maxima"]:
                    print(f'{dato}{espacios}')
                    # print(f'{float(day["heigth"]) + float(day["weight"]) + float(day["waistSize"])}{espacios}',end="")
                    # print(f'{round(((float(day["heigth"]) + float(day["weight"]) + float(day["waistSize"])) / 3),1)}{espacios}')
                else:
                    print(f'{dato}{espacios}',end="")
            
            columna += 1

printDay(diccionarioDias)
print("\nDias Registrados: ",len(diccionarioDias))
print("Dias con Datos Erroneos: ",diasErroneos)
print("  Datos Erroneos por Temperatura Minima: ",diasErroneosMin)
print("  Datos Erroneos por Temperatura Maxima: ",diasErroneosMax)
print("Proporcion de dias con errores: ",len(diccionarioDias) / diasErroneos, "|","1"," o del ", round(((1/(len(diccionarioDias) / diasErroneos)))*100,1), "%\n")
