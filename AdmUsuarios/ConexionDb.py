# mysql-connector-python
# pip install mysql-connector-python
# https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html

import mysql.connector
from Usuario import Usuario
from typing import List
class DAO:

    def __init__(self) -> None:
        self.cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='admusuarios')
        
    def VerificarUser(self)->Usuario:
        cursor = self.cnx.cursor()
        query = ("SELECT * FROM tbl_usuarios")
        cursor.execute(query)
        u = None
        for (rut, nombre, correo, rol, estado, contra) in cursor:
            u = Usuario(rut, nombre, correo, estado, rol, contra)
        return u
        
    def EliminarUsuario(self, rut:str):
        cursor = self.cnx.cursor()
        query = ("DELETE * FROM tbl_usuarios WHERE rut = %s")
        data = (rut,)
        cursor.execute(query, data)

    
    def FindUser(self, correo:str)->Usuario:
        cursor = self.cnx.cursor()
        query = ("SELECT * FROM tbl_usuarios WHERE correo = %s")
        data = (correo,)
        cursor.execute(query, data)
        if(cursor.rowcount == 0):
            cursor.reset()
            return None
        else: 
            for (rut, nombre, correo, rol, estado, contra) in cursor:
                u = Usuario(rut, nombre, correo, estado, rol, contra)
                cursor.reset()
                return u
    
    def FindUserByRut(self, rut:str)->Usuario:
        cursor = self.cnx.cursor()
        query = ("SELECT * FROM tbl_usuarios WHERE rut = %s")
        data = (rut,)
        cursor.execute(query, data)
        if(cursor.rowcount == 0):
            return None
        else: 
            for (rut, nombre, correo, rol, estado, contra) in cursor:
                u = Usuario(rut, nombre, correo, estado, rol, contra)
                return u

    def InsertarUsuario(self, u:Usuario)->None:
        cursor = self.cnx.cursor()
        query = ("INSERT INTO tbl_Usuarios (rut, nombre, correo, rol, estado, contra) VALUES (%s,%s,%s,%s,%s,%s)")
        data = (u.getRut(), u.getNombre(), u.getCorreo(), u.getRol(), u.getEstado(), u.getContra())
        cursor.execute(query, data)
        self.cnx.commit()
        cursor.reset()

    def CambiarContraseña(self, u:Usuario)->None:
        cursor = self.cnx.cursor()
        query = ("UPDATE tbl_Usuarios SET contra = %s WHERE rut = %s")
        data = (u.getContra(), u.getRut())
        cursor.execute(query, data)
        self.cnx.commit()
        cursor.reset()

    def BloquearUsuario(self, u:Usuario)->None:
        cursor = self.cnx.cursor()
        query = ("UPDATE tbl_Usuarios SET estado = %s WHERE rut = %s")
        data = ('bloqueado', u.getRut(),)
        cursor.execute(query, data)
        self.cnx.commit()
        cursor.reset()

    