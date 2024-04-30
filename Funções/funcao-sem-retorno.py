import os

# função sem retorno.
def senai():
    os.system("clear")
    print("==== SENAI ====")

# Solicitando dados para o usuario.
senai()
nome = input("Digite o seu nome: ")

senai()
idade = int(input("Digite a sua idade: "))

senai()
peso = float(input("Digite o seu peso: "))

#exibindo dados para o usuario.
senai()
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso}")
