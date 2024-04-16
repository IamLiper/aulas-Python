import os
os.system("clear")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

while nota1 and nota2 < 0 or nota1 and nota2 > 10:
    nota1 = float(input("Digite uma nota correta: "))
    nota2 = float(input("Digite a nota correta: "))
soma = nota1 + nota2
media = soma / 2
print(f"Nota1: {nota1}")
print(f"Nota2: {nota2}")
print(f"Média: {media}")