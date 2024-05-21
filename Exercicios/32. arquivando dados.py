import os
from dataclasses import dataclass

os.system("clear")

@dataclass
class Aluno:
    nome: str
    idade: int

QUANTIDADE_ALUNOS = 2

alunos = []

for i in range (QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome = input("Digite o seu nome: "),
        idade = int(input("Digite a sua idade: "))
    )
    alunos.append(aluno)
    os.system("clear")

# Definindo arquivo para salvar os dados
# inserido pelo usuário.
arquivo = "alunos.txt"

# Percorrendo o vetor e salvando os dados por linhas.
with open(arquivo, "w") as arquivoDeAlunos:
    for aluno in alunos:
        arquivoDeAlunos.write(f"{aluno.nome}, {aluno.idade} \n")

# Confirmando que os dados foram salvos.
print("Dados salvos com sucesso.")

for aluno in alunos:
    print(f"\nNome: {aluno.nome}")
    print(f"Idade: {aluno.idade}")