# 14. Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().

def filtrar_por_letra(lista_palabras, letra):
    return list(filter(lambda palabra: palabra.lower().startswith(letra.lower()), lista_palabras))

print(filtrar_por_letra(["router", "switch", "red", "servidor"], "r"))