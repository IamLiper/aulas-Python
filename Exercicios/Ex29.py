import os
os.system("cls || clear")
pares = 0
impares = 0
contador = 0
positivos = 0
negativos = 0

n = int(input(f"Digite o {contador +1}º número inteiro: "))
contador += 1
while n < 0 or n > 0: 
        n = int(input(f"Digite o {contador +1}º número inteiro: "))

        if n < 0 or n > 0:
            contador += 1
            if n > 0:
                positivos += 1
            if n < 0:
                negativos += 1
            if n % 2 == 0:
                pares += 1
            if n % 2 != 0:
                impares += 1

print(f"Quyantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")
print(f"Quantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}")
print(f"Quantidade de números inseridos: {contador}")
