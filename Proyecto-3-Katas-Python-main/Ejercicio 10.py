# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si está vacía, lanza una excepción personalizada...

class ErrorListaVacia(Exception):
    pass

def promedio_con_control(numeros):
    try:
        if not numeros:
            raise ErrorListaVacia("La lista está vacía.")
        return sum(numeros) / len(numeros)
    except ErrorListaVacia as error:
        print(f"Error detectado: {error}")
        return 0

print(promedio_con_control([]))