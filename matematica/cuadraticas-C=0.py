import math

valorA = int(input("Inserta el valor A: "))
valorB = int(input("Inserta el valor B: "))
raiz = math.sqrt(valorB * valorB)
print("El valor de X1 es igual a: ",(-valorB + raiz) / (2 * valorA))
print("El valor de X2 es igual a: ",(-valorB - raiz) / (2 * valorA))