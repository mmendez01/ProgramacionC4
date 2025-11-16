#Miguel Angel Mendez
respuesta = int(input("¿Hay internet? 1 = Sí, 0 = No: "))
estado = bool(respuesta)
if estado == True:
    print(f"Hay internet: {estado}")
else: 
    print(f"No hay internet: {estado}")