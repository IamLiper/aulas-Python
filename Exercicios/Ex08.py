import os

os.system("clear")

a = int
b = int
opcoes = 0

a = int(input("Digite o valor do A: "))
b = int(input("Digite o valor do B: "))
operacao = input("Digite um simbolo (+,-,*,/): ")

def opcoes(simbolo):
    if simbolo == '+':
        return a + b
    elif simbolo == '-':
        return a - b
    elif simbolo == '*':
        return a * b
    elif simbolo == '/':
        return a / b
    else:
        return 'Inválido.'

os.system("clear")

if operacao == '+':
    print("Soma: {}".format(opcoes(operacao)));
elif operacao == '-':
    print("Subtração: {}".format(opcoes(operacao)))
elif operacao == '*':
    print("Multiplicação: {}".format(opcoes(operacao)))
elif operacao == '/':
    print("Divisão: {}".format(opcoes(operacao)))
else:
    print(opcoes(operacao))