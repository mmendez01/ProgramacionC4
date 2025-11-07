Algoritmo FirewallSuperBasico
	
    // --- 1. Definición de Dimensiones y Constantes ---
    Definir DIM_IPS_BLOQUEADAS Como Entero;
    DIM_IPS_BLOQUEADAS <- 3;
    Definir MAX_LOG Como Entero;
    MAX_LOG <- 5; 
    Definir DIM_DATOS Como Entero;
    DIM_DATOS <- 4; // Col 1: IP, Col 2: Puerto, Col 3: Protocolo, Col 4: Estado
	
    // --- 2. Definición de Estructuras de Datos ---
    
    // Componente: Vector
    Definir ips_bloqueadas Como Cadena;
    Dimensionar ips_bloqueadas[DIM_IPS_BLOQUEADAS];
    
    // Componente: Matriz
    Definir log_general Como Cadena;
    Dimensionar log_general[MAX_LOG, DIM_DATOS];
    
    // Variable para contar cuántos paquetes van en el log
    Definir contador_log Como Entero;
    contador_log <- 0; // <-- CAMBIO (Empezamos en 0 items)
    
    // --- 3. Inicialización de Datos ---
    
    // Llenamos el vector de IPs bloqueadas
    ips_bloqueadas[1] <- "192.168.1.100"; // <-- CAMBIO (Índice 1)
    ips_bloqueadas[2] <- "10.0.0.5";      // <-- CAMBIO (Índice 2)
    ips_bloqueadas[3] <- "203.0.113.1"; // <-- CAMBIO (Índice 3)
    
    Escribir "--- Firewall Básico (Base-1) ---";
    Escribir "IPs Bloqueadas: ", ips_bloqueadas[1], ", ", ips_bloqueadas[2], ", ", ips_bloqueadas[3];
    Escribir "Vamos a registrar 3 paquetes.";
    Escribir "";
    
    // --- 4. Componente: Bucle (Simulación de 3 registros) ---
    Definir ip_origen, puerto, protocolo Como Cadena;
    Definir esta_bloqueado Como Logico;
	
    // Bucle para simular 3 registros
    Para i <- 1 Hasta 3 Hacer
        Escribir "--- Registrando Paquete #", i, " ---";
        
        // -- Pedir datos del paquete --
        Escribir "Ingrese IP de Origen:";
        Leer ip_origen;
        Escribir "Ingrese Puerto (ej: 80):";
        Leer puerto;
        Escribir "Ingrese Protocolo (TCP/UDP):";
        Leer protocolo;
        
        // -- Lógica de "RegistrarPaquete" (Bucle y Condicional) --
        esta_bloqueado <- Falso;
        Para j <- 1 Hasta DIM_IPS_BLOQUEADAS Hacer // <-- CAMBIO (Loop de 1 a 3)
            Si ip_origen = ips_bloqueadas[j] Entonces
                esta_bloqueado <- Verdadero;
            FinSi
        FinPara
        
        // Incrementamos el contador ANTES de usarlo como índice
        contador_log <- contador_log + 1; // <-- CAMBIO (Ahora contador_log es 1, 2, 3...)
        
        // -- Guardar en la MATRIZ --
        log_general[contador_log, 1] <- ip_origen;   // <-- CAMBIO (Columna 1)
        log_general[contador_log, 2] <- puerto;     // <-- CAMBIO (Columna 2)
        log_general[contador_log, 3] <- protocolo;  // <-- CAMBIO (Columna 3)
        
        Si esta_bloqueado Entonces
            log_general[contador_log, 4] <- "Bloqueado"; // <-- CAMBIO (Columna 4)
            Escribir " -> Resultado: PAQUETE BLOQUEADO.";
        Sino
            log_general[contador_log, 4] <- "Permitido"; // <-- CAMBIO (Columna 4)
            Escribir " -> Resultado: PAQUETE PERMITIDO.";
        FinSi
        
        Escribir "";
        
    FinPara
    
    // --- 5. Reportes (Bucle y Condicional) ---
    Escribir "Registro de 3 paquetes completo.";
    Escribir "---------------------------------";
    Escribir "";
	
    // Lógica de "MostrarRegistros"
    Escribir "--- Reporte de Paquetes Permitidos ---";
    Escribir "IP Origen | Puerto | Protocolo";
    Escribir "-------------------------------------";
    Para i = 1 Hasta contador_log Hacer // <-- CAMBIO (Loop de 1 a contador_log)
        // Condicional: Solo mostramos los "Permitidos"
        Si log_general[i, 4] = "Permitido" Entonces // <-- CAMBIO (Columna 4)
            Escribir log_general[i, 1], " | ", log_general[i, 2], " | ", log_general[i, 3]; // <-- CAMBIO (Cols 1,2,3)
        FinSi
    FinPara
    
    Escribir "";
    
    // Lógica de "GenerarAlertas"
    Escribir "--- Reporte de Alertas (Bloqueados) ---";
    Escribir "IP Origen | Puerto | Protocolo";
    Escribir "-------------------------------------";
    Para i = 1 Hasta contador_log Hacer // <-- CAMBIO (Loop de 1 a contador_log)
        // Condicional: Solo mostramos los "Bloqueados"
        Si log_general[i, 4] = "Bloqueado" Entonces // <-- CAMBIO (Columna 4)
            Escribir log_general[i, 1], " | ", log_general[i, 2], " | ", log_general[i, 3]; // <-- CAMBIO (Cols 1,2,3)
        FinSi
    FinPara
    Escribir "-------------------------------------";

FinAlgoritmo