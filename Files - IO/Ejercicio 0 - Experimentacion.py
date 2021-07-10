from io import open

archivo = open("Archivo Experimentacion.txt","w")
    # r read only
    # w write only
    # a add only
    # a+r add and read

cadena = "Universidad Sergio Arboleda"

# WRITE IN A FILE
archivo.write("Hoy es 6 de junio" + "\n" +cadena)

# OPEN FILE
archivo = open("Archivo Experimentacion.txt","r")

# READ A FILE
fileContent = archivo.read()
print(fileContent)

# ADJUST POINTER
archivo.seek(0)

# READ LINE TO LINE
fileContent = archivo.readlines()
print(fileContent)

# FOR IN A FILE
for i in fileContent:
    print(i)

# CLOSE FILE
archivo.close


# SECOND EXAMPLE
inputNumbers = []
strInputNumbers = ""
while True:
    inputNumbers.append(str(input("Ingrese un numero: ")))
    whileState = input("Desea agregar otro numero si(1) no(0): ")
    if whileState == "0":
        break

for x in inputNumbers:
    strInputNumbers += x

fileNumbers = open("Archivo Experimentacion - Numeros.txt","w")
fileNumbers.write(strInputNumbers)


