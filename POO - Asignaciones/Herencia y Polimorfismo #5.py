class Dispositivo:
    def encender(self):
        pass

class Laptop(Dispositivo):
    def encender(self):
        return "Laptop encendida: Iniciando sistema operativo y teclado retroiluminado."

class Telefono(Dispositivo):
    def encender(self):
        return "Teléfono encendido: Vibrando y mostrando pantalla de inicio."

# Ejemplo de uso
mis_dispositivos = [Laptop(), Telefono()]

for dispositivo in mis_dispositivos:
    print(dispositivo.encender())