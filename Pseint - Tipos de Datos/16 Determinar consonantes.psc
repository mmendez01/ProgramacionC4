Algoritmo Determinar_Consonantes
	
	Definir letra Como Caracter;
    
    Escribir "Ingrese una sola letra:";
    Leer letra;
    
    Si Longitud(letra) = 1 Entonces
        
        letra <- Minusculas(letra);
        
        Segun letra Hacer
            "a", "e", "i", "o", "u":
                Escribir "La letra ingresada es una VOCAL.";
            De Otro Modo:
                Escribir "La letra ingresada es una CONSONANTE.";
        FinSegun
        
    SiNo
        Escribir "Error: Debe ingresar solamente UNA letra.";
    FinSi
	
FinAlgoritmo
