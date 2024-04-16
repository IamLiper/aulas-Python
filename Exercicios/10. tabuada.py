i   mport os

os.system("clear")

numero = int(input("Digite um número: "))

os.system("clear")

print("=== Tabuada de multiplicação ===")
for i in range(10):
    print(f'{numero} x {i + 1} = {numero * (int(i) + 1)}')