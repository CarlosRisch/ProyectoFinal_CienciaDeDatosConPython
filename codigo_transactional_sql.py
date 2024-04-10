DDL_QUERY =  '''
CREATE TABLE categoria (
    idcategoria SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    descripcion VARCHAR(255),
    estado BOOLEAN
);

CREATE TABLE articulo (
    idarticulo SERIAL PRIMARY KEY,
    idcategoria INTEGER REFERENCES categoria(idcategoria),
    codigo VARCHAR(50),
    nombre VARCHAR(100),
    precio_venta NUMERIC(11, 2), 112.00
    stock INTEGER,
    descripcion VARCHAR(255),
    imagen VARCHAR(20),
    estado BOOLEAN
);

CREATE TABLE persona (
    idpersona SERIAL PRIMARY KEY,
    tipo_persona VARCHAR(20),
    nombre VARCHAR(100),
    tipo_documento VARCHAR(20),
    num_documento VARCHAR(20),
    direccion VARCHAR(70),
    telefono VARCHAR(20),
    email VARCHAR(50)
);

CREATE TABLE rol (
    idrol SERIAL PRIMARY KEY,
    nombre VARCHAR(30),
    descripcion VARCHAR(255),
    estado BOOLEAN
);

CREATE TABLE usuario (
    idusuario SERIAL PRIMARY KEY,
    idrol INTEGER REFERENCES rol(idrol),
    nombre VARCHAR(100),
    tipo_documento VARCHAR(20),
    num_documento VARCHAR(20),
    direccion VARCHAR(70),
    telefono VARCHAR(20),
    email VARCHAR(50),
    clave BYTEA,
    estado BOOLEAN
);

CREATE TABLE venta (
    idventa SERIAL PRIMARY KEY,
    idcliente INTEGER REFERENCES persona(idpersona),
    idusuario INTEGER REFERENCES usuario(idusuario),
    tipo_comprobante VARCHAR(20),
    serie_comprobante VARCHAR(7),
    num_comprobante VARCHAR(10),
    fecha TIMESTAMP,
    impuesto NUMERIC(4, 2),
    total NUMERIC(11, 2),
    estado VARCHAR(20)
);


CREATE TABLE detalle_venta (
    iddetalle_venta SERIAL PRIMARY KEY,
    idventa INTEGER REFERENCES venta(idventa),
    idarticulo INTEGER REFERENCES articulo(idarticulo),
    cantidad INTEGER,
    precio NUMERIC(11, 2),
    descuento NUMERIC(11, 2)
);

CREATE TABLE ingreso (
    idingreso SERIAL PRIMARY KEY,
    idproveedor INTEGER REFERENCES persona(idpersona),
    idusuario INTEGER REFERENCES usuario(idusuario),
    tipo_comprobante VARCHAR(20),
    serie_comprobante VARCHAR(7),
    num_comprobante VARCHAR(10),
    fecha TIMESTAMP,
    impuesto NUMERIC(4, 2),
    total NUMERIC(11, 2),
    estado VARCHAR(20)
);


CREATE TABLE detalle_ingreso (
    iddetalle_ing SERIAL PRIMARY KEY,
    idingreso INTEGER REFERENCES ingreso(idingreso),
    idarticulo INTEGER REFERENCES articulo(idarticulo),
    cantidad INTEGER,
    precio NUMERIC(11, 2)
);
'''