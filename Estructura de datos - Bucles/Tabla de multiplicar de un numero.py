numero_tabla = int(input("Ingresa un número para ver su tabla: "))

print(f"\n--- Tabla del {numero_tabla} ---")

for i in range(1, 11):
    resultado = numero_tabla * i
    print(f"{numero_tabla} x {i} = {resultado}")

print("--------------------")