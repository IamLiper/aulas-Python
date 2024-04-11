import os

os.system("cls || clear")

morango = str
maca = str
valorTotal = 0

escolha = str(input("Qual fruta você deseja:\n-1 Morango.\n-2 Maça.\nR= "))
kg = int(input("Quantos kg você deseja? "))
desconto = 10
if escolha == '1' and kg <= 5:
    valorTotal = (2.5 * kg)
elif escolha == '1' and kg > 5:
    valorTotal = (2.20 * kg)
if kg >= 8 and valorTotal > 25:
    valorTotal = valorTotal * desconto

if escolha == '2' and kg <= 5:
    valorTotal = (1.80 * kg)
elif escolha == '2' and kg > 5:
    valorTotal = (1.50 * kg)
if kg >= 8 and valorTotal > 25:
    valorTotal = valorTotal * desconto


print("Valor a ser pago pela {} será de R${}.".format(escolha, valorTotal))