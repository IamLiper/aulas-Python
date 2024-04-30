import os

def fnaf():
    os.system("clear")
    print("=== 🗿🗿🗿  ===")

def infla(inf):
    if inf < 100:
        return inf + (inf * (10 / 100))
    return inf + (inf * (20 / 100))

fnaf()
inflacao = float(input("Digite o preco do produto: "))

resultado = infla(inflacao)

print(f"Preço final: {resultado}")