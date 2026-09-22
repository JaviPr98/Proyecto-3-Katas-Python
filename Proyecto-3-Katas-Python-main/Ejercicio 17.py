from functools import reduce

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Usa la función reduce().

def digitos_a_numero(digitos):
    return reduce(lambda acumulado, digito: acumulado * 10 + digito, digitos)

print(digitos_a_numero([5, 7, 2]))