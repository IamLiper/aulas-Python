import os
os.system("cls || clear")

notas = []
soma = 0
contador = 0
QtdN = 0

for i in range(10):
    nota = float(input(f"Digite a sua nota {i+1}:"))
    notas.append(nota)
    contador += 1
    if nota < 0:
        QtdN += 1
    if nota >= 0:
        soma += nota
os.system("clear")

print(f"Soma positiva: {soma}")
print(f"Quantidade de números negativos: {QtdN}")
