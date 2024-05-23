import os
os.system("cls || clear")

pares = 0
impares = 0
positivos = 0
negativos = 0
contador = 0

for i in range(1, 6):
    n = int(input(f"Digite o {i}º número inteiro: "))
    contador += 1
    if n >= 0:
        positivos += 1
    else:
        negativos += 1
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Quyantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")
print(f"Quantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}")
print(f"Quantidade de números inseridos: {contador}")
