Algoritmo Ultimas_Letras
	
	Definir palabra, primeraLetra, ultimaLetra Como Caracter;
    Definir long Como Entero;
    
    Escribir "Ingrese una palabra:";
    Leer palabra;
    
    long <- Longitud(palabra);
    
    primeraLetra <- Subcadena(palabra, 1, 1);
    ultimaLetra <- Subcadena(palabra, long, long);
    
    Escribir "Palabra ingresada: ", palabra;
    Escribir "La primera letra es: ", primeraLetra;
    Escribir "La última letra es: ", ultimaLetra;
	
FinAlgoritmo
