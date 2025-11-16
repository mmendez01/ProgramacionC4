edad_usuario = int(input("Ingresa tu edad: "))

if edad_usuario < 0:
    print("Edad no válida. Ingresa un número positivo.")
elif edad_usuario < 13:
    print("Eres un niño.")
elif edad_usuario < 18:
    print("Eres un adolescente.")
elif edad_usuario < 65:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")