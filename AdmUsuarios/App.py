from Usuario import Usuario
from ConexionDb import DAO
import os


dao = DAO()
def Login(correo:str, contra:str)->bool:
    if(dao.VerificarUser() == None):
        user = Usuario('1-1', 'Admin', 'admin@inacap.cl', 'activo', 'SuperAdministrador', '123456')
        dao.InsertarUsuario(user)
    u = dao.FindUser(correo)
    if(u == None):
        return False
    else:
        if(contra == u.getContra()):
            if(u.getEstado() == "activo"):
                return u
            else:
                return u.getEstado()
        else:
            return False

while True:
    os.system("cls")
    print("============= Login ==============\n")
    correo = input("Ingresa tu Correo: ")
    contra = input("Ingresa Contraseña: ")

    usuarioLogueado = Login(correo, contra)
    if(usuarioLogueado == False):
        input("Credenciales Incorrectas!")
    if(usuarioLogueado == "bloqueado"):
        input("Usuario Bloqueado!")
    else:

        while True:
            os.system("cls")
            print("============Administracion de Usuarios=============\n")
            print("{1} . Crear nuevo Usuario")
            print("{2} . Eliminar Usuario")
            print("{3} . Actualizar Contraseña")
            print("{4} . Actualizar Datos de Usuario")
            print("{5} . Bloquear Usuario")
            print("{6} . Desbloquear Usuario")
            print("{7} . Ver Listado de Usuarios")
            print("{0} . Cerrar Sesion y Salir")

            op = input("Selecciona una Opcion: ")
    
            if(op == "0"):
                usuarioLogueado = None
                break

            if(op == "1"):
                os.system("cls")
                if(usuarioLogueado.getRol() == "SuperAdministrador" or usuarioLogueado.getRol() == "Administrador"):
                    r =input("Ingresa el Rut: ")
                    n =input("Ingresa el Nombre: ")
                    c =input("Ingresa el Correo: ")
                    rol =input("Ingresa el Rol: ")
                    cn = input("Ingresa la Contraseña: ")
                    u = Usuario(r,n,c, "activo", rol, cn)
                    dao.InsertarUsuario(u)
                    input("Usuario Creado! Presiona ENTER para Continuar...")
                else:
                    input("Permiso Denegado! Presiona ENTER para Continuar...")

            if(op == "2"):
                os.system("cls")
                r = input("Ingresa el Rut del Usuario: ")
                user = dao.FindUserByRut(r)
                if(user == None):
                    input("Usuario No existe! Presiona ENTER para Continuar...")
                if(user.getRol() == "SuperAdministrador"):
                    input("NO Puedes Eliminar un SuperAdministrador! Presiona ENTER para Continuar...")
                else:
                    dao.EliminarUsuario(r)
                    input("Usuario Eliminado! Presiona ENTER para Continuar...")

            if(op == "3"):
                os.system("cls")
                r = input("Ingresa el Rut del Usuario: ")
                user = dao.FindUserByRut(r)
                if(user == None):
                    input("Usuario No existe! Presiona ENTER para Continuar...")
                if(user.getRol() == "SuperAdministrador"):
                    input("NO Puedes cambiar contraseña a un SuperAdministrador! Presiona ENTER para Continuar...")
                else:
                    cn = input("Ingresa la Nueva Contraseña: ")
                    user.setContra(cn)
                    dao.CambiarContraseña(user)
                    input("Contraseña Actualizada! Presiona ENTER para Continuar...")

            if(op == "5"):
                os.system("cls")
                r = input("Ingresa el Rut del Usuario: ")
                user = dao.FindUserByRut(r)
                if(user == None):
                    input("Usuario No existe! Presiona ENTER para Continuar...")
                if(user.getRol() == "SuperAdministrador"):
                    input("NO Puedes Bloquear a un SuperAdministrador! Presiona ENTER para Continuar...")
                else:
                    dao.BloquearUsuario(user)
                    input("Usuario Bloqueado! Presiona ENTER para Continuar...")

