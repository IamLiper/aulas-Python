import os
os.system("cls")
class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

print("Solicitando dados para o usuário.")

cliente1 = Cliente("Marta", 20)

print(f"Nome: {cliente1.nome}")
print(f"Idade: {cliente1.idade}")