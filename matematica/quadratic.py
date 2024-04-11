import math

def quadraticFunction(exponentValue, crossValue, naturalValue, result, isResultCross):
    if((exponentValue, crossValue, naturalValue) != 0):
        quadraticSqrt = math.sqrt(crossValue ** 2 - 4 * exponentValue * naturalValue)
        firstResult = (-crossValue + quadraticSqrt) / (2 * exponentValue)
        secondResult = (-crossValue - quadraticSqrt) / (2 * exponentValue)
        return "First coordinate:", firstResult, "Second coordinate:", secondResult, "Type: All values"
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
        elif(result != 0 and isResultCross== False):
            naturalValue == -(result)
            quadraticSqrt = math.sqrt(crossValue ** 2 - 4 * exponentValue * naturalValue)
            firstResult = (-crossValue + quadraticSqrt) / (2 * exponentValue)
            secondResult = (-crossValue - quadraticSqrt) / (2 * exponentValue)
            return "First coordinate:", firstResult, "Second coordinate:", secondResult, "Type: Natural value imported from right side to left side"
        else:
            firstResult = (-crossValue + quadraticSqrt) / (2 * exponentValue)
            secondResult = (-crossValue - quadraticSqrt) / (2 * exponentValue)
            return "First coordinate:", firstResult, "Second coordinate:", secondResult, "Type: No natural value"

print(quadraticFunction(int(input()), int(input()), int(input())))
