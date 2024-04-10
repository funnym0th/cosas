import math

def quadraticFunction(exponentValue, xValue, naturalValue):
    if((exponentValue, xValue, naturalValue) != 0):
        quadraticSqrt = math.sqrt(xValue ** 2 - 4 * exponentValue * naturalValue)
        firstResult = (-xValue + quadraticSqrt) / 2 * exponentValue
        secondResult = (-xValue - quadraticSqrt) / 2 * exponentValue
        return firstResult, secondResult, "Type: All values"
    elif(xValue == 0, (exponentValue, naturalValue) != 0):
        quadraticSqrt = math.sqrt(- 4 * exponentValue * naturalValue)
        firstResult = (quadraticSqrt) / 2 * exponentValue
        secondResult = (-quadraticSqrt) / 2 * exponentValue
        return firstResult, secondResult, "Type: No bX value"
    elif(naturalValue == 0, (exponentValue, xValue) != 0):
        firstResult = (-xValue + quadraticSqrt) / 2 * exponentValue
        secondResult = (-xValue - quadraticSqrt) / 2 * exponentValue
        return firstResult, secondResult, "Type: No natural value"

print(quadraticFunction(int(input()), int(input()), int(input())))
