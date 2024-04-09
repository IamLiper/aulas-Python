import os

os.system("clear")

login = str
senha = str
loginCad = "Lipe"
senhaCad = "liper"

login = str(input("Digite seu login: "))
senha = str(input("Digite sua senha: "))

os.system("clear")

if login == loginCad and senha == senhaCad:
    print("Bem-Vindo!")
else:
    print("Login ou senha inválidos.")
