# 12. Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().

def longitud_palabras(frase):
    palabras = frase.split()
    return list(map(len, palabras))

print(longitud_palabras("redes y sistemas"))