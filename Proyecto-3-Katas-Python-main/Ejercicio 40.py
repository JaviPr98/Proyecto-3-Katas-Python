# 40. Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra...

def calcular_compra():
    precio_original = float(input("Precio original del artículo: "))
    tiene_cupon = input("¿Tienes cupón de descuento? (sí/no): ").strip().lower()

    if tiene_cupon in ["sí", "si"]:
        valor_cupon = float(input("Valor del cupón: "))
        if valor_cupon > 0:
            precio_final = max(0.0, precio_original - valor_cupon)
            print(f"Descuento aplicado. Precio final: {precio_final}€")
        else:
            print(f"Cupón no válido. Precio final: {precio_original}€")
    elif tiene_cupon == "no":
        print(f"Sin descuento. Precio final: {precio_original}€")
    else:
        print(f"Opción no válida. Precio original: {precio_original}€")