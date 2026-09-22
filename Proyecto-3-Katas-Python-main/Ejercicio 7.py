# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().

def tuplas_a_strings(lista_tuplas):
    return list(map(lambda tupla: " ".join(map(str, tupla)), lista_tuplas))

datos = [(1, "router"), (2, "switch")]
print(tuplas_a_strings(datos))