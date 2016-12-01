def getPotencia(potencia):
    return lambda x : x ** 2

cubo = getPotencia(3)

print cubo(2)
