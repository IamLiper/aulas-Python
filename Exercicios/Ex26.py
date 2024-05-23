import os
os.system("cls || clear")

valores = []

for i in range(5):
    valor = int(input(f"Digite o {i+1} valor: "))
    valores.append(valor)
    if valor < 0:
        valores[i] = 0

for i in range(len(valores)):
    print(f"Valores: {valores[i]}")