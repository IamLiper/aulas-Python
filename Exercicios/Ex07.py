import os

os.system("clear")

nomeP = str
qtdAdquirida = int
precoUni = 90
total = 0
totalApagar = 0
desconto = 0

qtdAdquirida = int(input("Digite a quantidade Que você deseja: "))

if qtdAdquirida <= 5:
    desconto = 18
elif qtdAdquirida > 5 and qtdAdquirida <= 10:
    desconto = 27
else:
    desconto = 45
    
total = qtdAdquirida * precoUni
totalApagar = total - desconto

print("Total a pagar: {}".format(totalApagar))