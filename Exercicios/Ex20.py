import os
os.system("cls || clear")

soma = 0
media = 0
contador = 0

while True:
    print("=== Menu ===")
    escolha = input("1. Adicionar\n2. Exibir resultado\n3. Sair\nR= ")
    if escolha == '1':
        idade = int(input("Digite sua idade: "))
        sexo = str(input("Informe o seu sexo (m/f): "))
        salario = float(input("nforme o seu sálario: "))
        contador += 1
    elif escolha == '2':
        soma += salario
        media =  soma / contador