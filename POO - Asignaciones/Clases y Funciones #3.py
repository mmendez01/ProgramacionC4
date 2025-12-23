class Coche:
    def __init__(self, marca, velocidad):
        self.marca = marca
        self.velocidad = velocidad

    def acelerar(self, incremento):
        self.velocidad += incremento


mi_coche = Coche("Toyota", 50)
mi_coche.acelerar(20)

print(f"Marca: {mi_coche.marca}")
print(f"Velocidad actual: {mi_coche.velocidad}")