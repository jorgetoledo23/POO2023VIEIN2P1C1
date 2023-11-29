CREATE DATABASE admusuarios;

USE admusuarios;


CREATE TABLE  tbl_usuarios (
    rut VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    correo VARCHAR(50) NOT NULL,
    rol VARCHAR(50) NOT NULL,
    estado VARCHAR(50) NOT NULL,
    contra VARCHAR(50) NOT NULL,
);