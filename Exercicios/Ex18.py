import os
os.system("clear")

nota: float = -1
soma: float = 0
contador: int = 0

while True:
    nota = float(input("Digite uma nota positiva: "))
    if nota >= 0:
        soma += nota
        contador += 1
    if nota < 0:
        break
print("Calculando...")

media = soma / contador

os.system("clear")
print("\n ===Resultado === \n")
print(f"Média: {media}")