from functools import reduce

# 22. Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().

def producto_total(numeros):
    return reduce(lambda a, b: a * b, numeros)

print(producto_total([2, 3, 4]))