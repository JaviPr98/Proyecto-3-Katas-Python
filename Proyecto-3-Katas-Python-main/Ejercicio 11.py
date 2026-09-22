# 11. Escribe un programa que pida al usuario que introduzca su edad...

def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("Edad fuera del rango permitido (0 a 120).")
        print(f"Edad correcta: {edad}")
    except ValueError as e:
        print(f"Entrada no válida: {e}")