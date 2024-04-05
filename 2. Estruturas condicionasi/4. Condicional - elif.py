import os

os.system("clear")

nota : float

nota = float(input("Digite sua nota: "))

if nota >= 7:
    print("Aprovado.")
elif nota >= 5:
    print("Recuperação.")
elif nota >= 4:
    print("Concelho de classe.")
else:
    print("Reprovado.")

print("=== FIM ===")