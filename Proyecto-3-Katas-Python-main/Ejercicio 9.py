# 9. Escribe una función que tome una lista de nombres de mascotas... Usa la función filter().

def filtrar_mascotas(mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda animal: animal not in prohibidas, mascotas))

animales = ["Perro", "Gato", "Tigre", "Loro", "Mapache"]
print(filtrar_mascotas(animales))