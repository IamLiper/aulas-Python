import os

os.system("clear")

login = str
senha = str
loginCad = "Lipe"
senhaCad = "liper"

login = str(input("Digite seu login: "))
senha = str(input("Digite sua senha: "))

os.system("clear")

while login != loginCad or senha != senhaCad:
    print("Login ou senha inválidos.")
    login = str(input("Digite seu login: "))
    senha = str(input("Digite sua senha: "))

os.system("clear")

print("Bem-Vindo!")