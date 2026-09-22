# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre y devuelva su puesto...

def obtener_puesto(nombre_completo, empleados):
    for emp in empleados:
        if emp["nombre"].lower() == nombre_completo.lower():
            return emp["puesto"]
    return "La persona no trabaja aquí"

lista_emp = [
    {"nombre": "Javier Ordóñez", "puesto": "Administrador de Redes"},
    {"nombre": "Ana Pérez", "puesto": "Analista de Seguridad"}
]
print(obtener_puesto("Javier Ordóñez", lista_emp))