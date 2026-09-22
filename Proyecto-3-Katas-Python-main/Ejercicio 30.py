# 30. Crea una función que determine si dos palabras son anagramas...

def son_anagramas(palabra1, palabra2):
    p1 = sorted(palabra1.replace(" ", "").lower())
    p2 = sorted(palabra2.replace(" ", "").lower())
    return p1 == p2

print(son_anagramas("roma", "amor"))