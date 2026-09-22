# 18. Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes y use filter para extraer a los estudiantes con calificación >= 90.

alumnos = [
    {"nombre": "Javier", "edad": 28, "calificacion": 95},
    {"nombre": "Carlos", "edad": 22, "calificacion": 80},
    {"nombre": "Lucía", "edad": 25, "calificacion": 91}
]

sobresalientes = list(filter(lambda x: x["calificacion"] >= 90, alumnos))
print(sobresalientes)