import os

def obanai():
    os.system("clear")
    print("=== 😶‍🌫️😶‍🌫️😶‍🌫️  ===")

def somarEmedia(n1, n2):
    resultado = (n1 + n2) / 2
    return resultado

obanai()
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

media = somarEmedia(numero1, numero2)

print(f"Média: {media}")