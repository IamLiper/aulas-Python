import os

def euglass():
    os.system("clear")
    print("=== 🗿🗿🗿  ===")

def cent(m):
    resultado = m * 100
    return resultado

euglass()
metros = int(input("Digite um valor em (metro): "))

resultado = cent(metros)

print(f"O metro convertido em centimetros: {resultado}")
