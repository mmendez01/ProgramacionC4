contraseña_correcta = "1234"
contraseña = ""

while contraseña != contraseña_correcta:
    contraseña = input("Ingresa la contraseña: ")
    if contraseña != contraseña_correcta:
        print("Incorrecta. Intenta de nuevo.")

print("¡Bienvenido!")