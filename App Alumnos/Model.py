from typing import List
class Alumno:
    """ Clase que define la estructura de un Alumno """
    def __init__(self, rut, nombre:str, apellido:str):
        self.Rut = rut
        self.Nombre = nombre.title() + " " + apellido.title() #jhon => Jhon
        self.LibroNotas:List[float] = []

    def getRut(self):
        return self.Rut

    def getFullName(self):
        return f"Rut: {self.Rut} Nombre: {self.Nombre}"
    
    def addNota(self, nota:float):
        self.LibroNotas.append(nota)
        input("Nota Ingresada!")
    
    def VerNotas(self):
        for nota in self.LibroNotas:
            print(nota)
        
    
    def getPromedio(self):
        """Metodo que retorna el Promedio de un Alumno"""
        if(len(self.LibroNotas) > 0):
            total:float = 0
            for nota in self.LibroNotas:
                total += nota
            return total / len(self.LibroNotas)
        return None
    