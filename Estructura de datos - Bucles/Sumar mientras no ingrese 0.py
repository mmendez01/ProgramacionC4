suma_total = 0.0
numero = -1

print("Ingresa números para sumar (ingresa 0 para terminar).")

while numero != 0:
    numero = float(input("Ingresa un número: "))
    suma_total = suma_total + numero

print(f"\nLa suma total es: {suma_total}")