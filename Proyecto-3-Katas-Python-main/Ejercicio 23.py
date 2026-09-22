# Concatena una lista de palabras. Usa la función reduce().
from functools import reduce

# 23. Concatena una lista de palabras. Usa la función reduce().

def unir_palabras(palabras):
    return reduce(lambda a, b: a + " " + b, palabras)

print(unir_palabras(["Sistemas", "Informáticos", "en", "Red"]))