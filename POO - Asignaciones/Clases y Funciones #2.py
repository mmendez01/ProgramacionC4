class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

mi_rectangulo = Rectangulo(10, 5)
area = mi_rectangulo.calcular_area()
print(f"El área es: {area}")