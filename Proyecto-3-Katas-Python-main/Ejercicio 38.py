# 38. Escribe un programa que determine qué calificación en texto tiene un alumno...

def calificacion_texto(nota):
    if 0 <= nota <= 69:
        return "insuficiente"
    elif 70 <= nota <= 79:
        return "bien"
    elif 80 <= nota <= 89:
        return "muy bien"
    elif 90 <= nota <= 100:
        return "excelente"
    return "nota fuera de rango"

print(calificacion_texto(95))