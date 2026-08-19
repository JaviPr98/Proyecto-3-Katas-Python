# Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.


def frecuencia_letra(texto):
    conteo= {}
    for letra in texto:
        if letra !=" ":
            #  Me costó entender que cuando se mete dentro del diccionario se suma 1 pero q tmb se mete la letra asociada
            if letra in conteo: 
                conteo[letra] += 1
            else: 
                conteo[letra] = 1
    return conteo

print (frecuencia_letra("hola como te llamas tu "))
