# 20. Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().

def obtener_solo_enteros(lista_mixta):
    return list(filter(lambda x: type(x) is int, lista_mixta))

print(obtener_solo_enteros([1, "hola", 2, "mundo", 3]))