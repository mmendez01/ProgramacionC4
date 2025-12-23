class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_bono(self):
        pass

class Gerente(Empleado):
    def calcular_bono(self):
        return self.salario * 0.20

class Tecnico(Empleado):
    def calcular_bono(self):
        return self.salario * 0.10

empleados = [
    Gerente("Xay", 3000),
    Tecnico("Zab", 2000)
]

for empleado in empleados:
    print(f"Empleado: {empleado.nombre} | Bono: {empleado.calcular_bono()}")