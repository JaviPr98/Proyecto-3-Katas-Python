# 27. Crea una función que calcule el promedio de una lista de números.

def calcular_promedio(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

print(calcular_promedio([8, 9, 10]))