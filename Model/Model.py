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

    def AgregarPost(self, texto, img):
        post = Post(img=img, texto=texto, user=self)
        self.Posts.append(post)
        input("Post Creado!")

    def VerPosts(self):
        print(f"Tienes {len(self.Posts)} Posts")
        for p in self.Posts:
            print(p.Texto)
            print(p.Imagen)
            print(f"Likes : {len(p.ListaLikes)}")
            print(f"Comentarios : {len(p.ListaComentarios)}")
            if(len(p.ListaComentarios) > 0):
                print("Comentarios: ")
                for c in p.ListaComentarios:
                    print(f"User: {c.Usuario.NombrePerfil} Comentario: {c.Texto}")

    def DarLike(self, p):
        like = Like(self, p)
        p.ListaLikes.append(like)
        input("Like Agregado!")

class Post:
    def __init__(self, user, texto, img):
        self.ListaComentarios = []
        self.ListaLikes = []
        self.Usuario = user
        self.Texto = texto
        self.Imagen = img

class Comentario:
    def __init__(self, user, comentario, post):
        self.Usuario = user
        self.Texto = comentario
        self.Post = post

class Like:
    def __init__(self, user, post):
        self.Usuario = user
        self.Post = post
        self.Fecha = datetime.datetime.now()

            
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
userLogueado = None

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
                userLogueado = user
            else:
                input("Contraseña Incorrecta")
                break
        
        if(not userLogueado == None):
            while True:
                print("[1] - Postear")
                print("[2] - Seguir")
                print("[3] - Ver Seguidores")
                print("[4] - Ver Seguidos")
                print("[5] - Ver Posts")
                print("[6] - Dar Like")
                print("[7] - Comentar Post")

                print("[0] - Cerrar Sesion")
                accion = input("Seleccione Accion: ")

                if(accion == "1"):
                    #Generar Post
                    os.system("cls")
                    t = input("Texto del Post: ")
                    img = input("Url de la Imagen: ")
                    userLogueado.AgregarPost(t,img)

                if(accion == "5"):
                    #Seguir
                    userLogueado.VerPosts()
                    input()

                if(accion == "6"):
                    os.system("cls")
                    for u in listaUsuarios:
                        if(len(u.Posts) > 0):
                            contador = 1
                            for p in u.Posts:
                                print(f"[{contador}] Usuario: {p.Usuario.NombrePerfil} Post: {p.Texto} Img: {p.Imagen}")
                                contador += 1
                    us = input("Usuario: ")
                    p = int(input("Numero Post: "))
                    usuario = None
                    for u in listaUsuarios:
                        if(u.NombrePerfil == us):
                            usuario = u

                    userLogueado.DarLike(usuario.Posts[p-1])
                    input()
                



#Task 1 : Obtener usuario logueado