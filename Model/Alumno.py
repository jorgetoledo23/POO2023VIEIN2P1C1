class Alumno:
    #Atributos => Estado
    def __init__(this, rut, nombre, apellido):
        this.Rut = rut
        this.Nombre = nombre
        this.Apellido = apellido

    #Metodos => Comportamiento
    def InsertarNota():
        pass
    
    def VerMisNotas():
        pass

    def GetInfo(this):
        return f"{this.Rut} {this.Apellido} {this.Nombre}"

class ExAlumno:
    Rut = None
    Nombre = None
    Apellido = None
    FechaEgreso = None


