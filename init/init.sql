CREATE TABLE Clientes (
    id_cliente VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    direccion VARCHAR(200)
);

CREATE TABLE Productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(300),
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL CHECK (stock >= 0)
);


CREATE TABLE Pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente VARCHAR(20) NOT NULL,
    fecha DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(12,2) NOT NULL DEFAULT 0,
    estado VARCHAR(20) NOT NULL DEFAULT 'PENDIENTE',
    metodo_pago VARCHAR(30),

    CONSTRAINT FK_Pedidos_Clientes
        FOREIGN KEY (id_cliente)
        REFERENCES Clientes(id_cliente)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE DetallePedido (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    subtotal DECIMAL(12,2) NOT NULL,

    CONSTRAINT FK_DetallePedido_Pedidos
        FOREIGN KEY (id_pedido)
        REFERENCES Pedidos(id_pedido)
        ON DELETE CASCADE,

    CONSTRAINT FK_DetallePedido_Productos
        FOREIGN KEY (id_producto)
        REFERENCES Productos(id_producto)
);



INSERT INTO Clientes (id_cliente, nombre, telefono, direccion) VALUES
('10000001','Ana Martínez','3001110001','Calle 10 #12-34'),
('10000002','Carlos López','3001110002','Carrera 15 #45-20'),
('10000003','María Gómez','3001110003','Calle 22 #18-10'),
('10000004','Juan Pérez','3001110004','Av 30 #25-80'),
('10000005','Laura Torres','3001110005','Calle 50 #60-12'),
('10000006','Andrés Ramírez','3001110006','Carrera 70 #33-14'),
('10000007','Paula Díaz','3001110007','Calle 80 #10-22'),
('10000008','Santiago Rojas','3001110008','Av 68 #44-19'),
('10000009','Camila Herrera','3001110009','Calle 90 #11-55'),
('10000010','Daniel Castro','3001110010','Carrera 12 #22-45'),
('10000011','Valentina Ruiz','3001110011','Calle 100 #15-40'),
('10000012','Sebastián Morales','3001110012','Av 7 #120-35'),
('10000013','Natalia Vega','3001110013','Carrera 50 #25-18'),
('10000014','Felipe Ortiz','3001110014','Calle 13 #40-50'),
('10000015','Gabriela Silva','3001110015','Av 19 #98-20'),
('10000016','Miguel Cárdenas','3001110016','Carrera 45 #70-33'),
('10000017','Daniela Mendoza','3001110017','Calle 75 #15-12'),
('10000018','Julián Romero','3001110018','Av 1 #33-90'),
('10000019','Isabella Navarro','3001110019','Calle 5 #20-10'),
('10000020','Mateo Vargas','3001110020','Carrera 88 #66-44');


INSERT INTO Productos (nombre, descripcion, precio, stock) VALUES
('Mouse Gamer','Mouse óptico RGB','85000',50),
('Teclado Mecánico','Teclado con switches rojos','250000',30),
('Monitor 24"','Monitor Full HD','750000',15),
('Laptop i5','Portátil 8GB RAM 512SSD','2800000',10),
('Audífonos Bluetooth','Cancelación de ruido','180000',40),
('Impresora HP','Impresora multifuncional','600000',12),
('Disco SSD 1TB','Alta velocidad','420000',25),
('Memoria USB 64GB','USB 3.0','35000',100),
('Silla Gamer','Silla ergonómica reclinable','900000',8),
('Webcam HD','Resolución 1080p','120000',35),
('Tablet 10"','Tablet Android','950000',14),
('Router WiFi','Doble banda','200000',20),
('Teclado Inalámbrico','Compacto','120000',22),
('Mouse Pad XL','Antideslizante','40000',60),
('Cámara Seguridad','Cámara IP','300000',18),
('Power Bank','10000 mAh','90000',45),
('Smartwatch','Reloj inteligente','350000',16),
('Micrófono USB','Para streaming','210000',13),
('Parlante Bluetooth','Portátil resistente','170000',28),
('Base Laptop','Base refrigerante','110000',32);


INSERT INTO Pedidos (id_cliente, total, estado, metodo_pago) VALUES
('10000001', 335000, 'PAGADO', 'TARJETA'),
('10000002', 85000, 'PENDIENTE', 'EFECTIVO'),
('10000003', 750000, 'ENTREGADO', 'TRANSFERENCIA'),
('10000004', 120000, 'PAGADO', 'NEQUI'),
('10000005', 180000, 'CANCELADO', 'EFECTIVO'),
('10000006', 900000, 'PAGADO', 'TARJETA'),
('10000007', 35000, 'ENTREGADO', 'TRANSFERENCIA'),
('10000008', 420000, 'PENDIENTE', 'TARJETA'),
('10000009', 200000, 'PAGADO', 'EFECTIVO'),
('10000010', 950000, 'PAGADO', 'TRANSFERENCIA');


INSERT INTO DetallePedido (id_pedido, id_producto, cantidad, subtotal) VALUES
(1,1,1,85000),
(1,5,1,180000),
(1,14,1,40000),
(2,1,1,85000),
(3,3,1,750000),
(4,10,1,120000),
(5,5,1,180000),
(6,9,1,900000),
(7,8,1,35000),
(8,7,1,420000),
(9,12,1,200000),
(10,11,1,950000);
