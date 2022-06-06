soluto = int(input("Inserte el valor del soluto: "))
solucion = int(input("Inserte el valor de la solución: "))
porcentaje = soluto/solucion * 100
decimal = input("Escribe el limite de decimales: ")
decimal = int(decimal)
porcentaje = round(porcentaje, (decimal))
print("El porcentaje aproximado del soluto en la solución es de", porcentaje,"%")