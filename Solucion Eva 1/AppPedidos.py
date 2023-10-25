import os
from typing import List
import datetime

class Producto:

    def __init__(self, codigo:str, nombre:str, descripcion:str, valorUnitario:int):
        self.Codigo = codigo
        self.Nombre = nombre
        self.Descripcion = descripcion
        self.Valor = valorUnitario

    def getInfo(self):
        return f"Codigo: {self.Codigo} | Nombre: {self.Nombre} | Descripcion: { self.Descripcion} | Valor Unitario: {self.Valor}"


class Pedido:
    def __init__(self, cod:int, clienteNombre:str, clienteTel:str):
         self.Codigo = cod
         self.NombreCliente = clienteNombre
         self.TelefonoCliente = clienteTel
         self.Fecha = datetime.datetime.now()
         self.Productos:List[Producto] = []

    def addProducto(self, producto:Producto, cantidad:int):
        producto.Cantidad = cantidad
        self.Productos.append(producto)
    
    def getInfo(self):
        print(f"Pedido Codigo: {self.Codigo}")
        print(f"Cliente: {self.NombreCliente} | Telefono: {self.TelefonoCliente}")
        Total = 0
        for p in self.Productos:
            print(f"{p.getInfo()} | Cantidad: {p.Cantidad}")
            Total += (p.Valor * p.Cantidad)
        print(f"\nTotal: {Total}")
        print("__________________________________________________________________________")


print("Bienvenido al Sistema de Notas")

listaProductos:List[Producto] = []
#productos por defecto
p1 = Producto("1-1", "Promo 1", "Papas XL + 2 Bebidas 350CC", 3990)
p2 = Producto("1-2", "Promo 2", "2 Completos + 2 Bebidas 350CC", 4990)
p3 = Producto("1-3", "Promo 3", "2 Churrascos + 2 Bebidas 350CC", 8990)
listaProductos.append(p1)
listaProductos.append(p2)
listaProductos.append(p3)

def BuscarProductoPorCodigo(cod:str):
    for p in listaProductos:
        if(p.Codigo == cod):
            return p


listaPedidos:List[Pedido] = []

while True:
    os.system("cls")
    print("[1] - Ingresar Productos")
    print("[2] - Ver Productos")
    print("[3] - Ingresar Pedido")
    print("[4] - Ver Pedidos")
    print("[0] - Salir")
    op = input("Selecciona una Opcion: ")

    if(op == "1"):
        os.system("cls")
        print("*******Ingreso de Productos*******\n")
        cod = input("Ingresa Codigo de Producto o Promocion: ")
        nom = input("Ingresa Nombre de Producto o Promocion: ")
        desc = input("Ingresa la Descripcion del Producto o Promocion: ")
        valor = input("Ingresa Valor del Producto o Promocion: ")
        p = Producto(cod, nom, desc, valor)
        listaProductos.append(p)
        input("Producto Agregado con Exito! Presiona Enter para Continuar...")

    if(op == "2"):
        os.system("cls")
        print("*******Listado de Productos*******\n")
        for p in listaProductos:
            print(p.getInfo())
        input("\nProductos y Promociones! Presiona Enter para Continuar...")

    if(op == "3"):
        os.system("cls")
        print("*******Generando Nuevo Pedido*******\n")

        nomCliente = input("Ingresa Nombre de Cliente: ")
        telCliente = input("Ingresa Telefono del Cliente: ")

        pedido = Pedido(len(listaPedidos)+1, nomCliente, telCliente)

        while True:
            os.system("cls")
            print(f"*******Generando Nuevo Pedido para: {nomCliente} | telefono: {telCliente} *******\n")

            cod = input("Ingresa el Codigo del Producto o Promocion: ")
            prod = BuscarProductoPorCodigo(cod)
            if( prod == None):
                input("Producto No Existe... Intenta Nuevamente!")
            else:
                print(f"Info Producto: {prod.getInfo()}")
                cantidad = int(input("Ingresa Cantidad deseada: "))
                pedido.addProducto(prod, cantidad)
                print("Producto/Promocion agregada con Exito!")

                continuar = input("Deseas agregar otro Producto o Promocion?: [S]Si / [N]No: ")
                if(continuar == "N"):
                    break
        os.system("cls")
        print("\n*******Pedido Generado! La Informacion del Pedido es:*******\n")
        print(f"Pedido para: {nomCliente} | telefono: {telCliente}")
        print("\nProductos/Promociones Incluidas:")
        Total = 0
        for p in pedido.Productos:
            print(f"{p.getInfo()} | Cantidad: {p.Cantidad}")
            Total += (p.Valor * p.Cantidad)
        print(f"\nTotal: {Total}")
        input("Gracias!")
        listaPedidos.append(pedido)


    if(op == "4"):
        os.system("cls")
        for p in listaPedidos:
            p.getInfo()
        input("\n**********Pedidos Listados**********")
