# 35. Crea la clase UsuarioBanco...

class UsuarioBanco:
    def __init__(self, nombre, saldo, tiene_cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.tiene_cuenta_corriente = tiene_cuenta_corriente

    def agregar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")
        self.saldo += cantidad

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente para transferir.")
        self.saldo -= cantidad
        otro_usuario.saldo += cantidad

# Caso de uso:
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)
bob.agregar_dinero(20)
if bob.saldo >= 80:
    bob.transferir_dinero(alicia, 80)
alicia.retirar_dinero(50)
print(f"Saldo Alicia: {alicia.saldo}, Saldo Bob: {bob.saldo}")