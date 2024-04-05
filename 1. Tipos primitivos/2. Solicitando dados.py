import os

os.system("cls || clear")

#Solicitando dados para o usuário.
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
telefone = int(input("Digite seu telefone: "))
data = int(input("Digite sua data de nascimento: "))
cpf = int(input("Digite seu CPF: "))

#Exibindo dados inseridos pelo usuário.
print("\n=== Exibindo resultados ===")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso:.3}")
print(f"Telefone: {telefone}")
print(f"Data de nascimento: {data}")
print(f"CPF: {cpf}")