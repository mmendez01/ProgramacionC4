total_notas = int(input("¿Cuántas notas deseas promediar?: "))

suma_total = 0.0

if total_notas > 0:
    for i in range(total_notas):
        calificacion = float(input(f"Ingresa la calificación {i + 1}: "))
        suma_total += calificacion

    promedio_final = suma_total / total_notas

    print(f"\nSe ingresaron {total_notas} notas.")
    print(f"El promedio final es: {promedio_final:.2f}")
else:
    print("No se ingresaron notas para calcular el promedio.")