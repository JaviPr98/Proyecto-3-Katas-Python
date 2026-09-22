# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.

def enmascarar_datos(variable):
    texto = str(variable)
    if len(texto) <= 4:
        return texto
    return "#" * (len(texto) - 4) + texto[-4:]

print(enmascarar_datos("4545123456789012"))