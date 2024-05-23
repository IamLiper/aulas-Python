import os

os.system("clear")

nome = str(input("Digite o seu nome: "))
idade = int(input("Digite a sua idade: "))
notas = []
i = 0
media = 0
soma = 0

for i in range (4):
    notasInput = float(input(f"Digite sua {i+1} nota: "))
    notas.append(notasInput)
    soma += notasInput
media = soma/ 4

print("=== Exibindo resultado ===")
print("Nome: {nome}")
print("Idade: {idade}")
print("Média: {:.1f}".format(media))

print("=== FIM ===")