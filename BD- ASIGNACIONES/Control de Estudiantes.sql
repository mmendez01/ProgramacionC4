CREATE DATABASE colegio;
USE colegio;

CREATE TABLE estudiantes (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    edad INT
);

CREATE TABLE cursos (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nombre_curso VARCHAR(100) NOT NULL,
    descripcion TEXT
);

CREATE TABLE matriculas (
    id_matricula INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT,
    id_curso INT,
    fecha_inscripcion DATE DEFAULT (CURRENT_DATE),
  
    FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id_estudiante) ON DELETE CASCADE,
    FOREIGN KEY (id_curso) REFERENCES cursos(id_curso) ON DELETE CASCADE
);

-- INSERCION --


INSERT INTO estudiantes (nombre, edad) VALUES 
('Xay', 8), --
('Zab', 4); --


INSERT INTO cursos (nombre_curso, descripcion) VALUES 
('Vuelo de Dragones Nivel 1', 'Introducción al vuelo con Furia Nocturna y Nader'),
('Mantenimiento de Cascos Multicolor', 'Cuidado y pintura de equipo de protección');


INSERT INTO matriculas (id_estudiante, id_curso) VALUES (1, 1), (1, 2);
INSERT INTO matriculas (id_estudiante, id_curso) VALUES (2, 1);
 
 
 -- CONSULTA --

SELECT 
    e.nombre AS Estudiante, 
    c.nombre_curso AS Curso,
    m.fecha_inscripcion AS "Fecha de Inicio"
FROM matriculas m
INNER JOIN estudiantes e ON m.id_estudiante = e.id_estudiante
INNER JOIN cursos c ON m.id_curso = c.id_curso;

SELECT 
    c.nombre_curso, 
    COUNT(m.id_estudiante) AS total_alumnos
FROM cursos c
LEFT JOIN matriculas m ON c.id_curso = m.id_curso
GROUP BY c.nombre_curso;