
CREATE DATABASE ventas;
USE ventas;

CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE
);

CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(150) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT DEFAULT 0
);

CREATE TABLE facturas (
    id_factura INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_producto INT,
    cantidad INT NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    -- Definición de relaciones (Claves Foráneas)
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- INSERTAR  DATOS -- 
INSERT INTO clientes (nombre, email) VALUES 
('Juan Pérez', 'juan.perez@email.com'),
('María García', 'm.garcia@email.com');

-- Insertar Productos
INSERT INTO productos (descripcion, precio, stock) VALUES 
('Laptop Pro 15', 1200.00, 10),
('Mouse Inalámbrico', 25.50, 50),
('Monitor 24 Pulgadas', 180.00, 15);

INSERT INTO facturas (id_cliente, id_producto, cantidad) VALUES 
(1, 1, 1),
(2, 3, 2);

-- CONSULTA --
SELECT 
    f.id_factura,
    c.nombre AS cliente,
    p.descripcion AS producto,
    f.cantidad,
    (f.cantidad * p.precio) AS total_pagar
FROM facturas f
INNER JOIN clientes c ON f.id_cliente = c.id_cliente
INNER JOIN productos p ON f.id_producto = p.id_producto;
