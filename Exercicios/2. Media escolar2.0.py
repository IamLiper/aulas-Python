import os

os.system("clear")

notas = []
i = 0
soma = 0
media = 0
produto = 0
maiorNum = 0
menorNum = 0
multiplicar = 0

for i in range (2):
    notasInput = float(input(f"Digite sua {i+1} nota: "))
    notas.append(notasInput)
    soma += notasInput
    
if notas[0] > notas[1]:
    maiorNum = notas[0]
    menorNum = notas[1]
else:
    maiorNum = notas[1]
    menorNum = notas[0]
multiplicar = notas[0] * notas[1]
media = soma/2
produto = multiplicar

print("=== Exibindo resultado ===")
print("Média: {:.1f}".format(media))
print("Soma: {}".format(soma))
print("Produto: {}".format(produto))
print("Maior número: {}".format(maiorNum))
print("Menor número: {}".format(menorNum))


print("=== FIM ===")