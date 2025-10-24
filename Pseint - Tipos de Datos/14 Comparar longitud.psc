Algoritmo Comparar_logitud_texto
	
	Definir cadena1, cadena2 Como Caracter;
    
    Escribir "Ingrese la primera cadena (palabra o frase):";
    Leer cadena1;
    
    Escribir "Ingrese la segunda cadena:";
    Leer cadena2;
    
    Si Longitud(cadena1) > Longitud(cadena2) Entonces
        Escribir "La primera cadena: " cadena1 " Es más larga";
    SiNo
        Si Longitud(cadena2) > Longitud(cadena1) Entonces
            Escribir "La segunda cadena: " cadena2  " Es más larga.";
        SiNo
            Escribir "Ambas cadenas tienen la misma longitud.";
        FinSi
    FinSi
	
FinAlgoritmo
