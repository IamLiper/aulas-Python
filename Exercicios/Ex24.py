import os
os.system("cls || clear")

numeros = []
maiorN = 0
menorN = 9999

for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    if numero > maiorN:
        maiorN = numero
    if numero < menorN:
        menorN = numero

for i in range(len(numeros)):
    print(f"{i+1}ª número: {numeros[i]}")
print(f"Maior número: {maiorN}")
print(f"Menor número: {menorN}")
