class CuentaBancaria:
    def __init__(self, titular, balance):
        self.titular = titular
        self.balance = balance

    def depositar(self, cantidad):
        self.balance += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
        else:
            print("Fondos insuficientes")


mi_cuenta = CuentaBancaria("Xay", 1000)
mi_cuenta.depositar(500)
mi_cuenta.retirar(200)

print(f"Titular: {mi_cuenta.titular}")
print(f"Saldo final: {mi_cuenta.balance}")