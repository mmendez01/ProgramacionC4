import time

inicio = int(input("Ingresa un número para iniciar la cuenta: "))

print(f"Cuenta regresiva desde {inicio}...")

while inicio >= 0:
    print(inicio)
    time.sleep(1) 
    inicio -= 1

print("¡Despegue!")