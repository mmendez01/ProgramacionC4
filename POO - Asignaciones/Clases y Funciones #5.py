class Estudiante:
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones

    def calcular_promedio(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)


estudiante1 = Estudiante("Xay", [85, 90, 78, 92])
promedio = estudiante1.calcular_promedio()

print(f"Estudiante: {estudiante1.nombre}")
print(f"Promedio de calificaciones: {promedio}")