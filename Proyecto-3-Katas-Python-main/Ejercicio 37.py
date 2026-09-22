# 37. Genera un programa que nos indique si es de noche, de día o de tarde según la hora...

def momento_del_dia(hora):
    if 6 <= hora < 14:
        return "Es de día"
    elif 14 <= hora < 21:
        return "Es de tarde"
    elif (21 <= hora <= 24) or (0 <= hora < 6):
        return "Es de noche"
    return "Hora no válida"

print(momento_del_dia(18))