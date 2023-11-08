from DbConnect import DAO
from Categoria import Categoria
import os

dao = DAO()
while True:
    os.system("cls")
    print("{1} . Insertar Nueva Categoria")
    print("{2} . Insertar Nuevo Producto")

    op = input("Selecciona una Opcion: ")

    if(op=="1"):
        nom = input("Nombre de la Categoria: ")
        Cat = Categoria(0, nom)
        dao.InsertarCategoria(Cat)
        input("Categoria Insertada! Presiona ENTER para Continuar...")