import os

os.system("clear")

valor1 = int
valor2 = int
valor3 = int
valor4 = int
valor5 = int
notas = []
soma = 0
pares = 0
impares = 0

for i in range (5):
    notasInput = float(input(f"Digite sua {i+1} nota: "))
    notas.append(notasInput)
    soma += notasInput

    if notas[i] % 2 == 0:
        pares += 1
    else:
        impares += 1


print("Soma de todos os números: {}".format(soma))
print("Pares: {}".format(pares))
print("Ímpares: {}".format(impares))