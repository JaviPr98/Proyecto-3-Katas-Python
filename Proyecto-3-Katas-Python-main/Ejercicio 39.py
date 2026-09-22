import math

# 39. Escribe una función que tome dos parámetros: figura y datos...

def calcular_area(figura, datos):
    figura = figura.lower()
    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        radio = datos[0]
        return math.pi * (radio ** 2)
    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    return "Figura no soportada"

print(calcular_area("rectangulo", (10, 5)))
print(calcular_area("circulo", (4,)))
