import math

def quadraticFunction(exponentValue, crossValue, naturalValue, result, isResultCross):
    if((exponentValue, crossValue, naturalValue) != 0):
        quadraticSqrt = math.sqrt(crossValue ** 2 - 4 * exponentValue * naturalValue)
        firstResult = (-crossValue + quadraticSqrt) / (2 * exponentValue)
        secondResult = (-crossValue - quadraticSqrt) / (2 * exponentValue)
        return "First coordinate:", firstResult, "Second coordinate:", secondResult, "Type: All val|ues"
    #EL SCRIPT SIN VALOR BX NO ESTA PREPARADO PARA RECIBIR UN VALOR BX DEL OTRO LADO DEL SIMBOLO IGUAL !!
    elif(crossValue == 0, (exponentValue, naturalValue) != 0):
        if(result != 0 and isResultCross == False):
            naturalValue = naturalValue -(result)
            quadraticSqrt = math.sqrt(- 4 * exponentValue * naturalValue)
            firstResult = quadraticSqrt / (2 * exponentValue)
            secondResult = -quadraticSqrt / (2 * exponentValue)
            return "First coordinate:", firstResult, "Second coordinate:", secondResult, "Type: No bX value, natural value imported from right side"
        else:
            quadraticSqrt = math.sqrt(- 4 * exponentValue * naturalValue)
            firstResult = quadraticSqrt / (2 * exponentValue)
            secondResult = -quadraticSqrt / (2 * exponentValue)
            return "First coordinate:", firstResult, "Second coordinate:", secondResult, "Type: No bX value"
    elif(naturalValue == 0, (exponentValue, crossValue) != 0):
        if(result != 0 and isResultCross == True):
            crossValue = crossValue -(result)
            quadraticSqrt = math.sqrt(- 4 * exponentValue * naturalValue)
            firstResult = (-crossValue + quadraticSqrt) / (2 * exponentValue)
            secondResult = (-crossValue - quadraticSqrt) / (2 * exponentValue)
            return "First coordinate:", firstResult, "Second coordinate:", secondResult, "Type: No natural value, BX value from right side imported to left side"
        elif(result != 0 and isResultCross == False):
            naturalValue == -(result)
            quadraticSqrt = math.sqrt(crossValue ** 2 - 4 * exponentValue * naturalValue)
            firstResult = (-crossValue + quadraticSqrt) / (2 * exponentValue)
            secondResult = (-crossValue - quadraticSqrt) / (2 * exponentValue)
            return "First coordinate:", firstResult, "Second coordinate:", secondResult, "Type: Natural value imported from right side to left side"
        else:
            firstResult = (-crossValue + quadraticSqrt) / (2 * exponentValue)
            secondResult = (-crossValue - quadraticSqrt) / (2 * exponentValue)
            return "First coordinate:", firstResult, "Second coordinate:", secondResult, "Type: No natural value"

print("Inserta los tres valores pertenecientes a una ecuacion cuadratica.\nSi el tipo de ecuacion deseada no comprende un valor BX o un valor natural C\ncoloca un 0 en su lugar. ")
print(quadraticFunction(int(input("Inserta el primer valor \"aX^2\":\n")), int(input("Inserta el segundo valor \"bX\":\n")), int(input("Inserta el tercer valor \"C\":\n")), int(input("Inserta el valor del resultado, si es que esta presente del otro lado del simbolo =\n Ejemplo: \"aX^2 + bX = c\" O \"aX^2 + bX = bX\":\n")), bool(input("Si el valor del resultado insertado previamente es bX, escribe \"True\" sin espacios y con la mayuscula.\nDe lo contrario, si es un numero natural escribe \"False\".\n"))))
