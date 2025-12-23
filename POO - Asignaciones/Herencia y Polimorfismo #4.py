class Vehiculo:
    def mover(self):
        pass

class Carro(Vehiculo):
    def mover(self):
        return "El carro se desplaza por la carretera usando un motor."

class Bicicleta(Vehiculo):
    def mover(self):
        return "La bicicleta se mueve pedaleando."

# Ejemplo de uso
transportes = [Carro(), Bicicleta()]

for transporte in transportes:
    print(transporte.mover())