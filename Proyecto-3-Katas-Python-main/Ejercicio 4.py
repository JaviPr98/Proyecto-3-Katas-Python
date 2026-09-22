# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def buscar_palabras_que_contienen(lista_palabras, palabra_objetivo):
    resultado = []
    for palabra in lista_palabras:
        if palabra_objetivo in palabra:
            resultado.append(palabra)
    return resultado

print(buscar_palabras_que_contienen(["ciberseguridad", "seguro", "redes", "antivirus"], "segur"))