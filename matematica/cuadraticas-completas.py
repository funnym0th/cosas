import math
valorA = int(input("Inserta el valor A: "))
valorB = int(input("Inserta el valor B: "))
valorC = int(input("Inserta el valor C: "))

raiz = math.sqrt(valorB * valorB - 4 * valorA * valorC)
divisor = 2 * valorA
print("El valor X1 de la ecuación es: ",(-valorB + raiz) / divisor)
print("El valor X2 de la ecuación es: ",(-valorB - raiz) / divisor)
