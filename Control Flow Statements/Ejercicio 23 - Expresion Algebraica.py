# 23 Construya un programa tal que dado como dato los valores enteros P y Q, determine si los mismos satisfacen la siguiente expresión:
#    P^3+Q^4-2*P^2<680, en caso afirmativo debe imprimir los valores P y Q.


print("Ingrese los valores que satisfacen la siguiente expresion: P^3 + Q^4-2 * P^2 < 680")
varP = int(input("Ingrese el valor de P: "))
varQ = int(input("Ingrese el valor de Q: "))

if ((varP**3) + ((varQ**4)-2) * (varP**2)) < 680:
    print(f"Los valores P={varP} y Q={varQ} satisfacen la expresion")

else:
    print("Los valores ingresados no satisfacen la expresion")
