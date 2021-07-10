valor1 = int(input('Ingrese el primer valor: '))
signo = str(input('Ingrese el signo de la operacion: '))
valor2 = int(input('Ingrese el segundo valor: '))

# Identificar singno
if signo == '+' :
    resultado = valor1 + valor2
if signo == '-' :
    resultado = valor1 - valor2
if signo == '*' :
    resultado = valor1 * valor2
if signo == '/' :
    resultado = valor1 / valor2
if signo == '%' :
    resultado = valor1 % valor2
if signo != '+' and signo != '-' and signo != '*' and signo != '/' and signo != '%' :
    resultado = '<<Error>>'

print(resultado)