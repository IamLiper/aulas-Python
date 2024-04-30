import os

# Função sem retorno.
def senai():
    os.system("clear")
    print("=== Vai uma coquinha? ===")

# Função com retorno.
def somar(n1, n2):
    coca = n1 + n2
    return coca

# Solicitando dados para o usuário.
senai()
primeiroNumero = int(input("Digite o primeiro valor: "))
segundoNumero = int(input("Digite o segundo valor: "))

soma = somar(primeiroNumero, segundoNumero)

# Exibindo dados para o usuário.
print(f"Duas coca R${soma}")
