class Producto:
    def __init__(self, cod:int, nombre:str, valor:int, stock:int, cod_categoria:int) -> None:
        self.__Cod_Producto = cod
        self.__NombreProducto = nombre
        self.__ValorUnitario = valor
        self.__Stock = stock
        self.__Cod_Categoria = cod_categoria
        self.__NombreCategoria = None

    def getCodProducto(self)->int:
        return self.__Cod_Producto
    
    def getNombre(self)->str:
        return self.__NombreProducto
    
    def getValor(self)->int:
        return self.__ValorUnitario
    
    def getStock(self)->int:
        return self.__Stock
    
    def getCodCategoria(self)->int:
        return self.__Cod_Categoria
    
    def setNombre(self, nuevoNombre:str):
        if(isinstance(nuevoNombre, str)):
            self.__NombreProducto = nuevoNombre.title()
        raise TypeError("Solo se permiten Strings")

    def setNombreCategoria(self, nombre):
        self.__NombreCategoria = nombre

    def getNombreCategoria(self)->str:
        return self.__NombreCategoria