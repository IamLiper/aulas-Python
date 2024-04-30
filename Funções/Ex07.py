import os

def gugu():
    os.system("clear")
    print("=== 🗿🗿🗿  ===")

def notaEmedia(n1, n2):
    resultado = (n1 + n2) / 2
    if resultado >= 7:
        print("Aprovado!")
    else:
        print("Reprovado!")
    return resultado

gugu()
nota1 = int(input("Digite a primeira nota: "))

gugu()
nota2 = int(iput("Digite a segunda nota: "))

resultado = notaEmedia(nota1, nota2)
