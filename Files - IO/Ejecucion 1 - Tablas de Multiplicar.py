# READ FILE
fileNumbersRead = open("Desarrollo Ejercicio 1.txt","r")
for number in fileNumbersRead:
    number = number.split(",")
    for x in number:
        print("\n")
        for y in range(1,11):
            print(x,"*",y,"=",int(x) * y)
    
