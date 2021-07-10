from io import open
import json

# OPEN FILE TXT
personsDataFileTxt = open("Desarrollo Ejercicio 2.txt","r")
personsDataTxt = personsDataFileTxt.readlines()
personsDatatxt = []
index = 0
data = 0
while data < len(personsDataTxt):
    personsDatatxt.append({})
    personsDatatxt[index]["name"] = personsDataTxt[data+0].replace("\n","")
    personsDatatxt[index]["heigth"] = personsDataTxt[data+1].replace("\n","")
    personsDatatxt[index]["weight"] = personsDataTxt[data+2].replace("\n","")
    personsDatatxt[index]["waistSize"] = personsDataTxt[data+3].replace("\n","")
    index += 1
    data += 5
    


# OPEN FILE JSON
personsDataFileJson = open("Desarrollo Ejercicio 2.json","r")
personsData = json.load(personsDataFileJson)

# PRINT
def printSubject(lista):
    encabezado = ["NOMBRE", "ESTATURA", "PESO", "TALLA CINTURA", "SUMATORIA MEDIDAS", "PROMEDIO MEDIDAS"]
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
    
    for subject in lista:
        columna = 0
        for dato in subject.values():
            longitudEncabezado = 0
            longitudDato = 0
            for long in range(len(encabezado[columna])):
                longitudEncabezado += 1
            for long in range(len(str(dato))):
                longitudDato += 1
            espacios = " " * ((longitudEncabezado + numeroEspacios) - longitudDato)

            if dato == subject['name']:
                print(f'{" " * 2}{dato}{" " * ((longitudEncabezado + 14) - longitudDato)}',end="")
            else:
                if dato == subject["waistSize"]:
                    print(f'{dato}{espacios}',end="")
                    print(f'{float(subject["heigth"]) + float(subject["weight"]) + float(subject["waistSize"])}{espacios}',end="")
                    print(f'{round(((float(subject["heigth"]) + float(subject["weight"]) + float(subject["waistSize"])) / 3),1)}{espacios}')
                else:
                    print(f'{dato}{espacios}',end="")
            
            columna += 1


print("IMPRESION DE DATOS POR EL ARCHIVO JSON")
printSubject(personsData)

print("\nIMPRESION DE DATOS POR EL ARCHIVO TXT")
printSubject(personsDatatxt)