import os

def jungwoo():
    os.system("clear")
    print("=== 🗿🗿🗿  ===")

def caall(n1, n2):
    print(f'Soma: {n1 + n2}')
    print(f'Sub: {n1 - n2}')
    print(f'Mult: {n1 * n2}')
    print(f'Divi: {(n1 / n2):.0f}')

jungwoo()
numero1 = int(input("Digite o primerio número: "))

jungwoo()
numero2 = int(input("Digite o segundo números: "))

print('Resultado:')
caall(numero1, numero2)
