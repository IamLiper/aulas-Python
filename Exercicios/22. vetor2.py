import os
os.system("cls || clear")

notas = []
soma = 0
contador = 0
for i in range(3):
    nota = float(input(f"Digite a sua {i+1}ª nota: "))
    notas.append(nota)
    soma += nota
    contador += 1
media = soma / contador 
print(f"Média: {media}")