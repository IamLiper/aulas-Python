import os

def ichiro():
    os.system("clear")
    print("=== 🗿🗿🗿  ===")

def tabuada(numero):
    for i in range(1, 11):
        print(f"{numero} * {i} = {numero * i}")

ichiro()
numero = int(input("Digite um número para a tabuada de multiplicação: "))

tabuada(numero)