Algoritmo DentroDeRango1_100
	
    Definir num Como Real;
    Definir estaEnRango Como Logico;
    
    Escribir "Ingrese un número:";
    Leer num;
    
    estaEnRango <- (num >= 1 Y num <= 100);
    
    Escribir "El resultado es: ", estaEnRango;
    
FinAlgoritmo