import requests
import time
import os
# pip install requests
os.system("cls")
while True:
    peticion = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    datos = peticion.json()
    precioBitcoinUSD = datos["bpi"]["USD"]["rate"]

    print(f"El precio actual del Bitcoin es: USD{precioBitcoinUSD}")
    time.sleep(5)