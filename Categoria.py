class Categoria:

    def __init__(self, cod:int, nombre:str) -> None:
        self.__CodigoCategoria = cod #Privada
        self.__Nombre  = nombre #Privada
    
    def getCodigoCategoria(self)->int:
        return self.__CodigoCategoria
    
    def getNombreCategoria(self)->str:
        return self.__Nombre