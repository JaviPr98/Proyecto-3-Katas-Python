# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().

def palabras_mas_largas(texto, n):
    palabras = texto.split()
    return list(filter(lambda p: len(p) > n, palabras))

print(palabras_mas_largas("el servidor proxy esta activo", 4))