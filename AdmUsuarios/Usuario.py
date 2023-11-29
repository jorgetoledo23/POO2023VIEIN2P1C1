class Usuario:

    def __init__(self, rut:str, nombre:str, correo:str, estado:str, rol:str, contra:str) -> None:
        self.__Rut = rut
        self.__Nombre = nombre
        self.__Correo = correo
        self.__Estado = estado
        self.__Contra = contra
        self.__Rol = rol

    def getRut(self)->str:
        return self.__Rut
    
    def getNombre(self)->str:
        return self.__Nombre
    
    def getCorreo(self)->str:
        return self.__Correo
    
    def getRol(self)->str:
        return self.__Rol
    
    def getEstado(self)->str:
        return self.__Estado
    
    def getContra(self)->str:
        return self.__Contra
    
    def setContra(self, nueva_contraseña):
        self.__Contra = nueva_contraseña