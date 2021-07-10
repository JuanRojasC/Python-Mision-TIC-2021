# 8. Construya un programa que muestre un mensaje a un usuario indicando el medio de transporte y la zona y zona sur que puede tomar de acuerdo al presupuesto que tiene.
#    zona norte
#    PRESUPUESTO	MEDIO DE TRANSPORTE
#    Entre  $8000 y  $10000	Moto
#    Entre  $11000 y $16000	Taxi
#    Entre  $17000 y $20000	Metro
#    Más de $20000	        uber
#    zona sur
#     PRESUPUESTO	MEDIO DE TRANSPORTE
#    Entre  $5000 y  $7000	Moto
#    Entre  $8000 y  $10000	Taxi
#    Entre  $11000 y $14000	Metro
#    Más de $14000 	        uber

presupuesto = int(input('\n Ingrese su presupuesto '))

# ZONA NORTE
if presupuesto >= 8000 and presupuesto < 10000 :
    transporteZonaNorte = 'Moto'
elif presupuesto >= 10000 and presupuesto < 16000 :
    transporteZonaNorte = 'Taxi'
elif presupuesto >= 16000 and presupuesto < 20000 :
    transporteZonaNorte = 'Metro'
elif presupuesto >= 20000 :
    transporteZonaNorte = 'UBER'

# ZONA SUR
if  5000 <= presupuesto < 7000 :
    transporteZonaSur = 'Moto'
elif 7000 <= presupuesto < 10000 :
    transporteZonaSur = 'Taxi'
elif 10000 <= presupuesto < 14000 :
    transporteZonaSur = 'Metro'
elif presupuesto >= 14000:
    transporteZonaSur = 'UBER'
 
print('\n\t En la zona norte el mejor medio de tranporte que puede tomar es', transporteZonaNorte)  
print('\t En la zona SUR el mejor medio de tranporte que puede tomar es', transporteZonaSur,'\n')  

