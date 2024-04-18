import os
os.system("clear")

notas = []
contador = 1
soma: float = 0
i = 0

notas = float(input(f"Digite a sua nota: "))


while (opcao == 's'):
    opcao = input("\nVocê add mais um? ")
    notas = float(input(f"Digite a {i+1}ª nota: "))
    contador + 1
    soma += notas

media = soma / contador

print(f"Média: {media:.1f}")
if media > 7:
    print("Aprovado!")
elif media >= 5 or media < 9:
    print("Recuperção!")
else:
    print("Reprovado!")