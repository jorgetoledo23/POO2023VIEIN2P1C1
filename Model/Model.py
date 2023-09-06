class Usuario:
    #Atributos 
    def __init__(self, cod, email, rol, nom, password, rut): #Constructor
        if(isinstance(cod, int)):
            self.Codigo = cod
        else:
            raise TypeError("El Codigo debe ser un numero Entero")
        self.Email = email
        self.Rol = rol
        self.Nombre = nom
        self.Password = password
        self.Rut = rut


Administrador = Usuario("1", "admin@gmail.com", "Admin", "Administrador", "123456", "1-1")
Auxiliar = Usuario(2, "aux@gmail.com", "Auxiliar", "Veronica", "1234", "2-K")

input("Ingresa Email: ")
print(Administrador.Email)