# Entradas
datos = str(input()).split()
salarioBase = float(datos[0])
horasExtras = float(datos[1])
bonificaciones = int(datos [2])


# Datos y Operaciones
valorHora = salarioBase / 190
valorHorasExtras = (valorHora * horasExtras) * 1.45
valorBonificaciones = salarioBase * 0.035

if valorHorasExtras > 0 and bonificaciones > 0 :
    salarioBruto = salarioBase + valorHorasExtras + valorBonificaciones
else :
    if valorHorasExtras > 0 :
        salarioBruto = salarioBase + valorHorasExtras 
    elif bonificaciones > 0 :
        salarioBruto = salarioBase + valorBonificaciones
    else :
        salarioBruto = salarioBase

# Descuentos
# Plan Obligatorio de Salud
planObligatorioSalud = salarioBruto * 0.065
# Aporte Pension
aportePension = salarioBruto * 0.05
# Caja de Compensacion
cajaCompensacion = salarioBruto * 0.04

salarioNeto = salarioBruto - (planObligatorioSalud + aportePension + cajaCompensacion)


# Salidas
print('{:.1f}'.format(salarioNeto),'{:.1f}'.format(salarioBruto))
