salarioMinimo = 908526
subsidioFamiliar = 40000

# Datos Cotizante
nombreApellido = str(input('Ingrese su nombre completo: '))
salario = int(input('Ingrese su salario mensual: '))
numeroHijos = int(input('Ingrese el numero de hijos: '))


# Cotizacion
if salario > (salarioMinimo*2) or salario == 0 :
    subsidioTransporte = 'No Aplica'
else :
    subsidioTransporte = 106454


# Subsidio Familiar   
if salario < (salarioMinimo*4) and salario != 0:
    subsidioFamiliar = subsidioFamiliar * numeroHijos
else :
    subsidioFamiliar = 'No Aplica'


# Aporte Salud
aporteSalud = round((salario/100) * 4)


# Aporte Pension
aportePension = round((salario/100) * 4)


# Total
pagos = aporteSalud + aportePension
total = (salario + subsidioTransporte + subsidioFamiliar) - pagos
print('\nCotizante: ',nombreApellido,'\nSubsidio Transporte: ',subsidioTransporte,'\nSubsidio Familiar: ',subsidioFamiliar,'\nAporte Salud: ',aporteSalud,'\nAporte Pension: ',aportePension,'\n\nTotal Aportes:',pagos,'\nTotal Ingreso:',total,'\n')