# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().

def doblar_valores(lista_numeros):
    return list(map(lambda x: x * 2, lista_numeros))

numeros = [1, 2, 3, 4, 5]
print(doblar_valores(numeros))