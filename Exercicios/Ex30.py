from cmath import inf
import os
os.system("cls || clear")
pares = 0
impares = 0
contador = 0
positivos = 0
negativos = 0
maiorN = 0
menorN = 999
soma = 0
somaP = 0
somaI = 0

n = int(input(f"Digite o {contador +1}º número inteiro: "))
contador += 1
while n < 0 or n > 0: 
        n = int(input(f"Digite o {contador +1}º número inteiro: "))

        if n < 0 or n > 0:
            contador += 1
            soma += n
            if n > 0:
                positivos += 1
            if n < 0:
                negativos += 1
            if n % 2 == 0:
                pares += 1
                somaP += n
            if n % 2 != 0:
                impares += 1
                somaI += n
            if n > maiorN:
                 maiorN = n
            if n < menorN:
                 menorN = n
        
mediaP = somaP / pares
mediaI = somaI / impares
media = soma / contador

print(f"Quyantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")
print(f"Quantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}")
print(f"Quantidade de números inseridos: {contador}")
print(f"Maior número: {maiorN}")
print(f"Menor número: {menorN}")
print(f"Média de pares: {mediaP}")
print(f"Média ímpares: {mediaI}")
print(f"Média geral: {media}")
for i in range(contador, 0, -1):
    print(i)
