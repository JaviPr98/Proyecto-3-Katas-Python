# 8. Escribe un programa que pida al usuario dos números e intente dividirlos...

def programa_division():
    try:
        numero1 = float(input("Primer número: "))
        numero2 = float(input("Segundo número: "))
        resultado = numero1 / numero2
        print(f"La división fue exitosa. Resultado: {resultado}")
    except ValueError:
        print("La división no fue exitosa: debes introducir un número.")
    except ZeroDivisionError:
        print("La división no fue exitosa: no se puede dividir entre cero.")