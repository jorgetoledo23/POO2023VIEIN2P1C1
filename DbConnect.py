# mysql-connector-python
# pip install mysql-connector-python
# https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html

import mysql.connector
from Categoria import Categoria
from Producto import Producto
class DAO:

    def __init__(self) -> None:
        self.cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='progra')
        
    def InsertarCategoria(self, Categoria:Categoria)->None:
        cursor = self.cnx.cursor()
        query = ("INSERT INTO CATEGORIAS (NOMBRE) VALUES (%s)")
        data = (Categoria.getNombreCategoria(),)
        cursor.execute(query, data)
        self.cnx.commit()

    def InsertarProducto(self, Producto:Producto)->None:
        cursor = self.cnx.cursor()
        query = ("INSERT INTO PRODUCTOS (COD_PRODUCTO, NOMBRE, VALOR_UNITARIO, STOCK, COD_CATEGORIA) VALUES (%s, %s, %s, %s, %s)")
        data = (Producto.getCodigo(), Producto.getNombre(), Producto.getValor())
        cursor.execute(query, data)
        self.cnx.commit()
