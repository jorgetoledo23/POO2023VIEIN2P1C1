#App para el ingreso de Alumnos a los cuales 
#se les podra ingresar una cantidad x de notas
#calcular automaticamente el promedio

import os
from typing import List
from Model import *

listaAlumnos:List[Alumno] = []

def BuscarAlumnoPorRut(rut:str):
    for a in listaAlumnos:
        if(a.getRut() == rut):
            return a

while 10==10:
    os.system("cls")
    print("[1] - Ingresar Alumnos al Sistema")
    print("[2] - Ver Alumnos ya Ingresados")
    print("[3] - Ingresar una Nota al Sistema")
    print("[4] - Ver Notas de un Alumno")
    print("[5] - Ver Promedio de un Alumno")
    print("[0] - Salir")
    opcion = input("Ingresa la Opcion seleccionada: ")

    if (opcion == "0"):
        break
    
    if(opcion == "1"):
        os.system("cls")
        r = input("Ingresa Rut del Alumno: ")
        n = input("Ingresa Nombre del Alumno: ")
        a = input("Ingresa Apellido del Alumno: ")
        alumno = Alumno(r,n,a)
        listaAlumnos.append(alumno)
        input("El Alumno se creo con exito!")
    
    if(opcion == "2"):
        os.system("cls")
        for alumno in listaAlumnos:
            print(alumno.getFullName())
        input()

    if(opcion == "3"):
        os.system("cls")
        r = input("Ingresa Rut del Alumno: ")
        alumno = BuscarAlumnoPorRut(r)
        if(alumno == None):
            input("Alumno No encontrado!")
        else:
            alumno.addNota(float(input("Ingresa la Nota: ")))
            input("Nota Ingresada al Sistema!")

    if(opcion == "4"):
        os.system("cls")
        r = input("Ingresa Rut del Alumno: ")
        alumno = BuscarAlumnoPorRut(r)
        if(alumno == None):
            input("Alumno No encontrado!")
        else:
            alumno.VerNotas()
            input()

    if(opcion == "5"):
        os.system("cls")
        r = input("Ingresa Rut del Alumno: ")
        alumno = BuscarAlumnoPorRut(r)
        if(alumno == None):
            input("Alumno No encontrado!")
        else:
            print(alumno.getPromedio())
            input()