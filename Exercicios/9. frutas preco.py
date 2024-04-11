import os

os.system("clear")

morango = str
maca = str
kgMo = 1
kgMa = 1
precoMokg = 2.5
precoMakg = 1.80

fruta = input("Digite a fruta que você escolheu: ")
if fruta == "morango":
    peso = int(input("Digite quantos kg deseja comprar de morango: "))
    if peso <= 5:
        preco = precoMokg * peso