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

for aluno in alunos:
    print(f"\nNome: {aluno.nome}")
    print(f"Idade: {aluno.idade}")