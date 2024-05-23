import os
from dataclasses import dataclass
os.system("clear")

funcionaros = []
QUANDIDADE_PESSOAS = 5
arquivo = 'Funcionarios.txt'

def salvar():
    for i in range(QUANDIDADE_PESSOAS):
        funcionario = Funcionarios(
            nome = input("Digite o nome do funcionário: "),
            data_nascimento = input("Digite a data de nascimento do funcionário: "),
            rg = input("Digite o rg do funcionário: "),
            cpf = input("Digite o cpf do funcionário: ")
        )
        funcionaros.append(funcionario)
        os.system("clear")

    with open(arquivo, "w") as arquivoDeFuncionarios:
        for funcionario in funcionaros:
            arquivoDeFuncionarios.write(f"\nNome: {funcionario.nome}\nData de Nascimento: {funcionario.data_nascimento}\nRG: {funcionario.rg}\nCPF: {funcionario.cpf} \n")

        print("Os dados foram salvos com sucesso!")

def ler_dados_salvos():
    with open(arquivo, "r") as arquivosDeFunconarios:
        funcionarios_cad = arquivosDeFunconarios.read()
    print(funcionarios_cad)

@dataclass
class Funcionarios:
    def __init__(self, nome, data_nascimento, rg, cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.rg = rg
        self.cpf = cpf

salvar()
ler_dados_salvos()