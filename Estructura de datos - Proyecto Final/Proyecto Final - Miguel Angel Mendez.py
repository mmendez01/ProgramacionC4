def simulador_firewall():
    
    ips_bloqueadas = ["192.168.1.100", "10.0.0.5", "203.0.113.1"]
    log_general = []

    print("--- Firewall Básico (Python) ---")
    print(f"IPs Bloqueadas: {', '.join(ips_bloqueadas)}")
    print("Vamos a registrar 3 paquetes.\n")

    
    for i in range(1, 4):
        print(f"--- Registrando Paquete #{i} ---")
        
        ip_origen = input("Ingrese IP de Origen: ")
        puerto = input("Ingrese Puerto (ej: 80): ")
        protocolo = input("Ingrese Protocolo (TCP/UDP): ")

       
        estado = "Permitido"
        if ip_origen in ips_bloqueadas:
            estado = "Bloqueado"
            print(" -> Resultado: PAQUETE BLOQUEADO.")
        else:
            print(" -> Resultado: PAQUETE PERMITIDO.")

        log_general.append([ip_origen, puerto, protocolo, estado])
        print("")

    print("Registro de 3 paquetes completo.")
    print("-" * 35)

    # --- 3. Generación de Reportes ---
    encabezado = f"{'IP Origen':<15} | {'Puerto':<6} | {'Protocolo'}"

    # Reporte de Permitidos
    print("\n--- Reporte de Paquetes Permitidos ---")
    print(encabezado)
    print("-" * 35)
    for fila in log_general:
        if fila[3] == "Permitido":
            print(f"{fila[0]:<15} | {fila[1]:<6} | {fila[2]}")

    # Reporte de Bloqueados (Alertas)
    print("\n--- Reporte de Alertas (Bloqueados) ---")
    print(encabezado)
    print("-" * 35)
    for fila in log_general:
        if fila[3] == "Bloqueado":
            print(f"{fila[0]:<15} | {fila[1]:<6} | {fila[2]}")
            
    print("-" * 35)

if __name__ == "__main__":
    simulador_firewall()