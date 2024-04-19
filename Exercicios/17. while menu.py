import os
os.system("clear")

notas: float = - 1
soma: float = 0
QtdNotas = 0

while True:

    print ("\n=== MENU ===\n")
    print("S- Inserir notas: ")
    print("P- Ver a quantidade de notas inseridas: ")
    print("N- Calcular média arimética: ")

    resposta = input("Insira uma nota: ")
    if resposta == "S":
        notas= float(input("\nInforme uma nota: "))
        soma += notas
        QtdNotas += 1
    elif resposta == "P":
        if QtdNotas == 0:
            print("Não foram inserida as notas! ")
        else:
            print (f"Quantidade de notas inseridas: {QtdNotas}\n")

    elif resposta == 'N':
        media = soma / QtdNotas
        print(f"Média: {media}")
        if QtdNotas == 0:
            print("Não foram inseridas notas. \n")
        else:
            print("Opção inválida... \n")

