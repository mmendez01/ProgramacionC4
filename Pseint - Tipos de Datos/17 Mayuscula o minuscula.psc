Algoritmo Determinar_mayuscula_minuscula
	
	Definir caracter Como Caracter;
    
    Escribir "Ingrese un carácter:";
    Leer caracter;
    
    Si Longitud(caracter) = 1 Entonces
        
        Si caracter = Mayusculas(caracter) Y caracter <> Minusculas(caracter) Entonces
            Escribir "El carácter " caracter " es MAYÚSCULA.";
        SiNo
            Si caracter = Minusculas(caracter) Y caracter <> Mayusculas(caracter) Entonces
                Escribir "El carácter " caracter " es MINÚSCULA.";
            SiNo
                Escribir "El carácter " caracter " no es una letra (es un número o símbolo).";
            FinSi
        FinSi
        
    SiNo
        Escribir "Error: Debe ingresar solo UN carácter.";
    FinSi
	
FinAlgoritmo
