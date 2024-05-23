import os

os.system("clear")

nome = str
idade = int

nome = str(input("Digite seu nome: "))
idade = int(input("Diigte sua idade: "))

os.system("clear")

if idade > 18 and idade < 65:
    print(f"Obrigado a votar.")
else:
    print("Não obrigado a votar")