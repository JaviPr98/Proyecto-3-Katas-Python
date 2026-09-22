# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar...

def buscar_nombre():
    entrada = input("Nombres separados por comas: ")
    nombres = [n.strip() for n in entrada.split(",")]
    buscado = input("Nombre a buscar: ").strip()
    
    if buscado in nombres:
        print(f"'{buscado}' encontrado en la lista.")
    else:
        raise ValueError(f"'{buscado}' no está en la lista.")