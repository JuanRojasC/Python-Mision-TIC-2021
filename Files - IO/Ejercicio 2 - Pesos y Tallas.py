# * crear un programa que lea n datos de n personas (nombre estaura, talla y peso).
#   y alamacene estos datos en un archivo "datosper.txt".
#   abra el archivo el y muestre los datos de cada persona. sumatoria y promedio de 
#   estatura peso y talla.
from io import open
import json

# FUNCTIONS
def verifyFloat(entry):
    numberFloat = 0
    try:
        numberFloat = float(entry)
    except ValueError:
        numberFloat = 'INVALID DATA'
    return numberFloat

# VARIABLES
index = 0
personsData = []

# EXECUTION
while True:
    # SUBJECT NAME
    subjectName = str(input('Nombre: '))
    # SUBJECT HEIGTH
    subjectHeigth = verifyFloat(input('Estatura (CM): '))
    while subjectHeigth == "INVALID DATA":
        subjectHeigth = verifyFloat(input('\tIngrese Estatura Valida: '))
    # SUBJECT WEIGHT
    subjectWeight = verifyFloat(input("Peso (KG):"))
    while subjectWeight == "INVALID DATA":
        subjectWeight = verifyFloat(input("\tIngrese Peso Valido: "))
    # SUBJECT WAIST SIZE
    subjectWaistSize = verifyFloat(input("Talla de la Cintura: "))
    while subjectWaistSize == "INVALID DATA":
        subjectWaistSize = verifyFloat(input("\tIngrese Talla de la Cintura Valida: "))

    # OBJECT PERSON
    personsData.append({})
    personsData[index]["name"] = subjectName
    personsData[index]["heigth"] = subjectHeigth
    personsData[index]["weight"] = subjectWeight
    personsData[index]["waistSize"] = subjectWaistSize

    # DATA FOR TXT FILE AND CREATE A FILE TXT
    personsDataTxt = str(subjectName) + "\n" + str(subjectHeigth) + "\n" + str(subjectWeight) + "\n" + str(subjectWaistSize) + "\n" + "\n"
    
    if index == 0:
        personsDataFileTxt = open("Desarrollo Ejercicio 2.txt", "w")
        personsDataFileTxt.write(personsDataTxt)
        personsDataFileTxt.close
    else:
        personsDataFileTxt = open("Desarrollo Ejercicio 2.txt", "a")
        personsDataFileTxt.write(personsDataTxt)
        personsDataFileTxt.close

    # CONTINUE ADD DATA
    whileBreak = str(input("Desea agregar otro sujeto si(1) no(0): "))
    while whileBreak != "0" and whileBreak != "1":
        whileBreak = str(input("\tIngrese una opcion valida: "))
    if whileBreak == "0":
        break

    index += 1


# CREATE A FILE JSON
personsDataFile = open("Desarrollo Ejercicio 2.json","w")
personsDataFile.write(json.dumps(personsData))
personsDataFile.close

    