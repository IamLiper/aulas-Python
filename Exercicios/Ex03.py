import os

os.system("clear")

nota1 = int
nota2 = int
media = 0
soma = 0
produto = 0
maiorNum = 0
menorNum = 0
valorIgual = 0

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

if nota1 > nota2:
    maiorNum = nota1
    menorNum = nota2
else:
    maiorNum = nota2
    menorNum = nota1

if nota1 == nota2:
    valorIgual = nota1
else:
    valorIgual = nota2    

soma = nota1 + nota2
produto = nota1 * nota2
media = soma /2

print("Média: {:.1f}".format(media))
print("Soma: {}".format(soma))
print("Produto: {}".format(produto))
print("Maior número: {}".format(maiorNum))
print("Menor número: {}".format(menorNum))