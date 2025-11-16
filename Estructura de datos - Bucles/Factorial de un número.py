num = int(input("Ingresa un número para ver su factorial: "))

resultado = 1

if num < 0:
    print("No existe factorial para números negativos.")
elif num == 0:
    print("El factorial de 0 es 1.")
else:
    for i in range(1, num + 1):
        resultado *= i
    
    print(f"El factorial de {num} es {resultado}")