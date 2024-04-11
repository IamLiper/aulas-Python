import os

os.system("clear")

soma = 0


for i in range(1, 6):
    num = int(input("Digite um número inteiro: "))
    soma += num
print(f"Soma de todos os números inteiros: {soma}")