import requests
import os
os.system("cls")

n = input("Ingresa nombre del Pokemon: ")
try:
    peticion = requests.get(f"https://pokeapi.co/api/v2/pokemon/{n}")
    #print(peticion.status_code)
    datos = peticion.json()

    print("\nTipo(s) del Pokemon: ")
    tipos = datos["types"]
    for tipo in tipos:
        print(tipo["type"]["name"])

    print("\nMovimientos que puede Aprender: ")
    movimientos = datos["moves"]
    
except:
    print("Pokemon NO Encontrado!")