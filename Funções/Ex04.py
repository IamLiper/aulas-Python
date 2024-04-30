import os

def xeng():
    os.system("clear")
    print("=== 🗿🗿🗿  ===")

def parOuImpar(numero):
    if numero % 2 == 0:
        print(f"{numeros} é par.")
    else:
        print(f"{numeros} é ímpar.")

xeng()
numeros = int(input("Digite um número: "))

parOuImpar(numeros)