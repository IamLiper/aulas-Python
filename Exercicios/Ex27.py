import os
os.system("cls || clear")

valores = []

for i in range (1, 7):
    valor = int(input(f"Digite o {i}º valor: "))
    valores.append(valor)
    if valor < 0:
        valor = int(input("Digite um valor inteiro: "))
for i in range(6, 0, -1):
    print(i)