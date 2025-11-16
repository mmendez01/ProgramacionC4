#Miguel Angel Mendez

import random

numero_secreto = random.randint(1, 20)
adivinanza = 0
intentos = 0

print("Adivina el número secreto (entre 1 y 20)")

while adivinanza != numero_secreto:
    adivinanza = int(input("¿Cuál es tu número?: "))
    intentos += 1
    
    if adivinanza < numero_secreto:
        print("El número secreto es más alto.")
    elif adivinanza > numero_secreto:
        print("El número secreto es más bajo.")
    else:
        print(f"¡Felicidades! Adivinaste en {intentos} intentos.")