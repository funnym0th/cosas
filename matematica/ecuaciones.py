import math

tipoEcuacion = int(input("1) Ecuacion completa \n2) Ecuacion sin BX \n3) Ecuacion sin C \nElegir tipo de ecuacion: "))
if tipoEcuacion == 1:
    valorA = int(input("Inserta el valor A: "))
    valorB = int(input("Inserta el valor B: "))
    valorC = int(input("Inserta el valor C: "))
    raiz = math.sqrt(valorB**2 - 4 * valorA * valorC)
    divisor = 2 * valorA
    print("El valor X1 de la ecuación es: ",(-valorB + raiz) / divisor)
    print("El valor X2 de la ecuación es: ",(-valorB - raiz) / divisor)
elif tipoEcuacion == 2:
    valorA = int(input("Inserta el valor A: "))
    valorC = int(input("Inserta el valor C: "))
    raiz = math.sqrt(-4 * valorA * valorC)
    divisor = 2 * valorA
    print("El resultado de X1 es: ", (0 + raiz)/divisor)
    print("El resultado de X2 es: ", (0 - raiz)/divisor)
elif tipoEcuacion == 3:
    valorA = int(input("Inserta el valor A: "))
    valorB = int(input("Inserta el valor B: "))
    raiz = math.sqrt(valorB**2)
    print("El valor de X1 es igual a: ",(-valorB + raiz) / (2 * valorA))
    print("El valor de X2 es igual a: ",(-valorB - raiz) / (2 * valorA))
