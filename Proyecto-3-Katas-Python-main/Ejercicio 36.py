# 36. Crea una función llamada procesar_texto...

def contar_palabras(texto):
    frecuencias = {}
    for p in texto.lower().split():
        frecuencias[p] = frecuencias.get(p, 0) + 1
    return frecuencias

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra_a_eliminar):
    palabras = texto.split()
    return " ".join([p for p in palabras if p != palabra_a_eliminar])

def procesar_texto(texto, opcion, *argumentos):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, argumentos[0], argumentos[1])
    elif opcion == "eliminar":
        return eliminar_palabra(texto, argumentos[0])
    return "Opción inválida"

print(procesar_texto("servidor web servidor dns", "contar"))