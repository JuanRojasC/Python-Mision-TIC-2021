# Entrada de datos
consumokwh = int(input('Consumo en Kwh: '))

# Cotizacion
if consumokwh < 1000 :
    valorFactura = consumokwh * 1.2
if 1000 <= consumokwh <= 1850 :
    valorFactura = consumokwh * 1.0
if consumokwh > 1850 :
    valorFactura = consumokwh * 0.9

print('El valor de su facuta electrica es de: ',valorFactura)