import os

os.system("clear")

idade : int

idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Não votar.")
elif idade < 18 or idade >= 65:
    print("Não obrigado a votar.")    
else:
    print("Pode votar.")

print("=== FIM ===")  