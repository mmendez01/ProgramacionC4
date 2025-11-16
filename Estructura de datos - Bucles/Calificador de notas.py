puntuacion = float(input("Introduce tu calificación (0-10): "))

if puntuacion < 0 or puntuacion > 10:
    print("Error: La calificación debe estar entre 0 y 10.")
elif puntuacion >= 9.0:
    print("Calificación: Sobresaliente (A)")
elif puntuacion >= 7.0:
    print("Calificación: Notable (B)")
elif puntuacion >= 5.0:
    print("Calificación: Aprobado (C)")
else:
    print("Calificación: Suspenso (F)")