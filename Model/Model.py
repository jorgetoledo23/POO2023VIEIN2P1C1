import datetime
import os

class Usuario:
    #Atributos 
    def __init__(self, email, nom, nomperfil, password): #Constructor
        self.Email = email
        self.Nombre = nom
        self.NombrePerfil = nomperfil
        self.Password = password
        self.Seguidores = []
        self.Seguidos = []
        self.Posts = []
        self.BandejaEntrada = []
    
    def Seguir(self, seguido):
        self.Seguidos.append(seguido)
        seguido.Seguidores.append(self)

    def EnviarMensaje(self, destinatario, mensaje):
        M = Mensaje(self, destinatario, mensaje)
        destinatario.BandejaEntrada.append(M)

    def VerSeguidos(self):
        os.system("cls")
        print(f"tienes { len(self.Seguidos) } seguidos")
        for S in self.Seguidos:
            print(S.NombrePerfil)

    def VerSeguidores(self):
        os.system("cls")
        print(f"tienes { len(self.Seguidores) } seguidores")
        for S in self.Seguidores:
            print(S.NombrePerfil)

    def VerMensajes(self):
        os.system("cls")
        for M in self.BandejaEntrada:
            print(f"De: {M.Remitente.NombrePerfil} Mensaje: {M.Mensaje}")
            
class Mensaje:
    def __init__(self, user, destinatario, mensaje):
        self.Remitente = user
        self.Destinatario = destinatario
        self.Mensaje = mensaje
        self.Fecha = datetime.datetime.now()
        self.Estado = "No Leido"

colocolooficial = Usuario("colocolochile@cc.cl", "Colo Colo", "Colo Colo Oficial", "1234")
messi = Usuario("messi@fifa.com", "Lionel Messi", "LioMessi", "1234")
elbicho = Usuario("elbicho@cr7.com", "Cristiano Ronaldo", "Cristiano", "1234")
m14 = Usuario("m14@chile.cl", "Matias Fernandez", "Matigol", "1234")

# m14.EnviarMensaje(colocolooficial, "Paguen lo que me deben")
# messi.EnviarMensaje(colocolooficial, "Contratenme por favor!")

# colocolooficial.VerMensajes()


listaUsuarios = [colocolooficial, messi, elbicho, m14]

while True:
    os.system("cls")
    print("[1] - Registro")
    print("[2] - Iniciar Sesion")
    opcion = input("Selecciona una Opcion: ")
    if(opcion == "1"):
        os.system("cls")
        n = input("Ingresa Nombre: ")
        c = input("Ingresa Correo: ")
        u = input("Ingresa Nombre de Perfil: ")
        p = input("Ingresa una Contraseña: ")
        newUser = Usuario(c, n, u, p)
        listaUsuarios.append(newUser)
        input("Usuario registrado!")
    if(opcion == "2"):
        os.system("cls")
        correo = input("Ingresa tu Correo: ")
        user = None
        for U in listaUsuarios:
            if(U.Email == correo):
                user = U
        if(user == None):
            input("No Existe ese Usuario")
        else:
            os.system("cls")
            contra = input("Ingrese Contraseña: ")
            if(user.Password == contra):
                input("Inicio de Sesion Correcto!")
            else:
                input("Contraseña Incorrecta")
