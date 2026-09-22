# 13. Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().

def letras_tuplas(cadena):
    sin_espacios = cadena.replace(" ", "")
    letras_unicas = set(sin_espacios)
    return list(map(lambda letra: (letra.upper(), letra.lower()), letras_unicas))

print(letras_tuplas("hola"))