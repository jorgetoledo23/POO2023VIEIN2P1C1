# mysql-connector-python
# pip install mysql-connector-python
# https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html

import mysql.connector
from Categoria import Categoria
from Producto import Producto
from typing import List
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

    def EliminarCategoria(self, cod:int)->None:
        cursor = self.cnx.cursor()
        query = ("DELETE FROM categorias WHERE cod_categoria = %s")
        data = (cod,)
        cursor.execute(query, data)
        self.cnx.commit()

    def ActualizarCategoria(self, asd:Categoria)->None:
        cursor = self.cnx.cursor()
        query = ("UPDATE categorias SET nombre = %s WHERE cod_categoria = %s")
        data = (asd.getNombreCategoria(), asd.getCodigoCategoria())
        cursor.execute(query, data)
        self.cnx.commit()


    def InsertarProducto(self, Producto:Producto)->None:
        cursor = self.cnx.cursor()
        query = ("INSERT INTO PRODUCTOS (COD_PRODUCTO, NOMBRE, VALOR_UNITARIO, STOCK, COD_CATEGORIA) VALUES (%s, %s, %s, %s, %s)")
        data = (Producto.getCodProducto(), Producto.getNombre(), Producto.getValor(), Producto.getStock(), Producto.getCodCategoria())
        cursor.execute(query, data)
        self.cnx.commit()

    def LeerCategorias(self)->List[Categoria]:
        cursor = self.cnx.cursor()
        query = ("SELECT * FROM categorias")
        cursor.execute(query)

        categoriasList:List[Categoria] = []
        for (cod_categoria, nombre) in cursor:
            cat = Categoria(cod_categoria, nombre)
            categoriasList.append(cat)
        return categoriasList
    
    def LeerProductos(self)->List[Producto]:
        cursor = self.cnx.cursor()
        query = ("""SELECT P.cod_producto, P.nombre, P.valor_unitario, P.stock, C.nombre AS 'nombre_categoria', P.cod_categoria
                 FROM Productos P INNER JOIN Categorias C ON P.cod_categoria = C.cod_categoria""")
        cursor.execute(query)

        ProductosList:List[Producto] = []
        for (cod_producto, nombre, valor_unitario, stock, nombre_categoria, cod_categoria) in cursor:
            pro = Producto(cod_producto, nombre, valor_unitario, stock, cod_categoria)
            pro.setNombreCategoria(nombre_categoria)
            ProductosList.append(pro)
        return ProductosList