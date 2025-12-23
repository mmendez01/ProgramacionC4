# --- 1. Definición de Dimensiones y Constantes ---
DIM_IPS_BLOQUEADAS = 3
MAX_LOG = 5
DIM_DATOS = 4  # Col 0: IP, Col 1: Puerto, Col 2: Protocolo, Col 3: Estado

# --- 2. Definición de Estructuras de Datos ---
# En Python usamos listas. Inicializamos el log como una lista vacía.
ips_bloqueadas = [""] * DIM_IPS_BLOQUEADAS
log_general = [] # Usaremos una lista de listas para representar la matriz

# --- 3. Inicialización de Datos ---
ips_bloqueadas[0] = "192.168.1.100"
ips_bloqueadas[1] = "10.0.0.5"
ips_bloqueadas[2] = "203.0.113.1"

print("--- Firewall Básico (Base-0) ---")
print(f"IPs Bloqueadas: {', '.join(ips_bloqueadas)}")
print("Vamos a registrar 3 paquetes.\n")

# --- 4. Bucle (Simulación de 3 registros) ---
for i in range(1, 4):
    print(f"--- Registrando Paquete #{i} ---")
    
    # -- Pedir datos del paquete --
    ip_origen = input("Ingrese IP de Origen: ")
    puerto = input("Ingrese Puerto (ej: 80): ")
    protocolo = input("Ingrese Protocolo (TCP/UDP): ")
    
    # -- Lógica de "RegistrarPaquete" --
    esta_bloqueado = False
    if ip_origen in ips_bloqueadas:
        esta_bloqueado = True
        
    # -- Guardar en la MATRIZ (como una fila/lista) --
    estado = "Bloqueado" if esta_bloqueado else "Permitido"
    # Guardamos los datos en una lista que representa la fila de la matriz
    paquete = [ip_origen, puerto, protocolo, estado]
    log_general.append(paquete)
    
    if esta_bloqueado:
        print(" -> Resultado: PAQUETE BLOQUEADO.")
    else:
        print(" -> Resultado: PAQUETE PERMITIDO.")
    print("")

# --- 5. Reportes ---
print("Registro de 3 paquetes completo.")
print("---------------------------------\n")

# Lógica de "MostrarRegistros" (Permitidos)
print("--- Reporte de Paquetes Permitidos ---")
print("IP Origen      | Puerto | Protocolo")
print("-------------------------------------")
for registro in log_general:
    if registro[3] == "Permitido":
        print(f"{registro[0]:<14} | {registro[1]:<6} | {registro[2]}")

print("\n--- Reporte de Alertas (Bloqueados) ---")
print("IP Origen      | Puerto | Protocolo")
print("-------------------------------------")
for registro in log_general:
    if registro[3] == "Bloqueado":
        print(f"{registro[0]:<14} | {registro[1]:<6} | {registro[2]}")
print("-------------------------------------")