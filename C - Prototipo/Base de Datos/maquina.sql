CREATE DATABASE maquina;
USE maquina;

CREATE TABLE TipoProducto (
    id INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE Sabor (
    id INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE Consistencia (
    id INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE Estado (
    id INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE MaquinaHelado (
    id INT PRIMARY KEY,
    id_estado INT,
    id_tipo INT,
    id_sabor INT,
    id_consistencia INT,
    FOREIGN KEY (id_estado) REFERENCES Estado(id),
    FOREIGN KEY (id_tipo) REFERENCES TipoProducto(id),
    FOREIGN KEY (id_sabor) REFERENCES Sabor(id),
    FOREIGN KEY (id_consistencia) REFERENCES Consistencia(id)
);

-- Insertar estados
INSERT INTO Estado (id, nombre) VALUES
(1, 'Apagada'),
(2, 'Encendida'),
(3, 'En Producción');

-- Insertar tipos de producto
INSERT INTO TipoProducto (id, nombre) VALUES
(1, 'Helado'),
(2, 'Batido');

-- Insertar sabores
INSERT INTO Sabor (id, nombre) VALUES
(1, 'Vainilla'),
(2, 'Dulce de Leche'),
(3, 'Combinado');

-- Insertar consistencias
INSERT INTO Consistencia (id, nombre) VALUES
(1, 'Suave'),
(2, 'Media'),
(3, 'Cristalizado');

-- Insertar máquinas de helado
INSERT INTO MaquinaHelado (id, id_estado, id_tipo, id_sabor, id_consistencia) VALUES
(1, 1, 1, 1, 1),
(2, 2, 1, 2, 2),
(3, 3, 2, 3, 3),
(4, 1, 1, 1, 2),
(5, 2, 2, 2, 1),
(6, 3, 1, 3, 2),
(7, 1, 2, 1, 3);
