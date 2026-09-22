# 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5)...

def evaluar_notas(notas, nota_aprobado=5):
    media = sum(notas) / len(notas)
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
    return (media, estado)

print(evaluar_notas([6, 7, 8, 5]))