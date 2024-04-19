import os
os.system("cls || clear")

valores = []

for i in range (2):
    valor = int(input(f"Digite o {i+1}º valor: "))
    valores.append(valor)
    if valor != int:
        valor = int(input("Digite um valor inteiro: "))
    elif valor >= 0:
    