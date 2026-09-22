# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    return numero * factorial(numero - 1)

print(factorial(5))