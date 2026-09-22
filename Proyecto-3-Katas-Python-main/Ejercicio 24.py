from functools import reduce

# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().

def diferencia_total(numeros):
    return reduce(lambda a, b: a - b, numeros)

print(diferencia_total([100, 20, 10]))