from DbConnect import DAO
from Categoria import Categoria
from Producto import Producto
import os

dao = DAO()
while True:
    os.system("cls")
    print("{1} . Insertar Nueva Categoria")
    print("{2} . Insertar Nuevo Producto")
    print("{3} . Leer Categorias Guardadas")
    print("{4} . Leer Productos Guardados")
    print("{5} . Eliminar Categoria")
    print("{6} . Actualizar Categoria")

    op = input("Selecciona una Opcion: ")

    if(op=="5"):
        os.system("cls")
        for cat in dao.LeerCategorias():
            print(f"{cat.getCodigoCategoria()} | {cat.getNombreCategoria()}")
        perrito = input("Ingresa el Codigo de la Categoria a eliminar: ")
        dao.EliminarCategoria(perrito)
        input("Categoria Eliminada! Presiona ENTER para Continuar...")

    if(op=="6"):
        os.system("cls")
        for cat in dao.LeerCategorias():
            print(f"{cat.getCodigoCategoria()} | {cat.getNombreCategoria()}")
        perrito = input("Ingresa el Codigo de la Categoria a actualizar: ") 
        nuevoNombre = input("Ingresa el nuevo nombre de la Categoria: ")
        cat = Categoria(perrito, nuevoNombre)
        dao.ActualizarCategoria(cat)
        input("Categoria Actualizada! Presiona ENTER para Continuar...")

    if(op=="1"):
        nom = input("Nombre de la Categoria: ")
        Cat = Categoria(0, nom)
        dao.InsertarCategoria(Cat)
        input("Categoria Insertada! Presiona ENTER para Continuar...")

    if(op=="3"):
        os.system("cls")
        for cat in dao.LeerCategorias():
            print(f"{cat.getCodigoCategoria()} | {cat.getNombreCategoria()}")
        input("Categorias Listadas! Presiona ENTER para continar...")

    if(op=="2"):
        os.system("cls")
        for cat in dao.LeerCategorias():
            print(f"{cat.getCodigoCategoria()} | {cat.getNombreCategoria()}")
        cat = input("Seleccione Codigo de Categoria: ")
        os.system("cls")
        cod = input("Ingresa el Codigo Unidco del Producto: ")
        nom = input("Nombre del Producto: ")
        precio = input("Valor Unitario del Producto: ")
        stock = input("Ingrese Stock Disponible del Producto: ")
        p = Producto(cod, nom, precio, stock, cat)
        dao.InsertarProducto(p)
        input("Producto Guardado! Presiona ENTER para continuar...")

    if(op=="4"):
        os.system("cls")
        for pro in dao.LeerProductos():
            print(f"{pro.getCodProducto()} | {pro.getNombre()} | {pro.getValor()} | {pro.getStock()} | {pro.getNombreCategoria()}")
        input("Productos Listados! Presiona ENTER para continar...")
