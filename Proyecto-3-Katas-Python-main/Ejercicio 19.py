# 19. Crea una función lambda que filtre los números impares de una lista dada.

filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))

print(filtrar_impares([1, 2, 3, 4, 5, 6, 7]))