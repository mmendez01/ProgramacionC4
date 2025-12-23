CREATE DATABASE biblioteca;
USE biblioteca;
CREATE TABLE autores (
    id_autor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    edad INT
);

CREATE TABLE libros (
    id_libro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    genero VARCHAR(50),
    id_autor INT,
   
    FOREIGN KEY (id_autor) REFERENCES autores(id_autor) 
    ON DELETE CASCADE
);

INSERT INTO autores (nombre, edad) VALUES ('Xay', 8); --
INSERT INTO autores (nombre, edad) VALUES ('Zab', 4); --

INSERT INTO libros (titulo, genero, id_autor) VALUES 
('Las aventuras de Lila la Furia Nocturna', 'Fantasía', 1), 
('El vuelo del Nader Rojo', 'Aventura', 2),                  
('Guía del Casco Multicolor', 'Manual', 1);                 

SELECT libros.titulo, autores.nombre AS escritor
FROM libros
INNER JOIN autores ON libros.id_autor = autores.id_autor;