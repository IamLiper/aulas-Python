import os
from dataclasses import dataclass

os.system("clear")

@dataclass
class Aluno:
    nome: str
    idade: int
    peso: float
    altura: float

QUANTIDADE_ALUNOS = 2

alunos = []

for i in range (QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome = input("Digite o seu nome: "),
        idade = int(input("Digite a sua idade: ")),
        peso = float(input("Digite o seu peso: ")),
        altura = float(input("Digite a sua altura: "))
    )
    alunos.append(aluno)
    os.system("clear")

# Definindo arquivo para salvar os dados
# inserido pelo usuário.
arquivo = "Dados_pessoais.txt"

# Percorrendo o vetor e salvando os dados por linhas.
with open(arquivo, "w") as arquivoDeAlunos:
    for aluno in alunos:
        arquivoDeAlunos.write(f"{aluno.nome}, {aluno.idade}, {aluno.peso}, {aluno.altura} \n")

# Confirmando que os dados foram salvos.
print("Dados salvos com sucesso.")

for aluno in alunos:
    print(f"\nNome: {aluno.nome}")
    print(f"Idade: {aluno.idade}")
    print(f"Peso: {aluno.peso}")
    print(f"Altura: {aluno.altura}")