# VARIABLES
dataNumber = int(input())
listDataPrint = []
dataPrinted = 0

# EXECUTION
for informationLine in range(dataNumber):
    yearsOld, experienceYears, languagesQuantity, certificationsQuantity, salaryHope = input().split(" ")
    if 25 <= int(yearsOld) < 40 and int(experienceYears) >= 5 and int(languagesQuantity) >= 3 and int(certificationsQuantity) > 4:
        dataPrinted += 1
        listDataPrint.append(salaryHope)
        
if len(listDataPrint) == 0:
    print("NO DISPONIBLE")
else:
    for aspirant in listDataPrint:
        print(aspirant)


        