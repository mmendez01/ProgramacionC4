Algoritmo EsNumero
    
    Definir caracter Como Caracter;
    
    Escribir "Ingrese un carácter:";
    Leer caracter;
    
    Si Longitud(caracter) = 1 Entonces
        
        Si caracter >= "0" Y caracter <= "9" Entonces
            Escribir "El carácter " caracter " ES un número.";
        SiNo
            Escribir "El carácter " caracter " NO es un número.";
        FinSi
        
    SiNo
        Escribir "Error: Debe ingresar solo UN carácter.";
    FinSi
    
FinAlgoritmo