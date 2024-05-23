import os
from dataclasses import dataclass
os.system("clear")

def ler_dados_catalogo():
    with open(arquivo, "r") as arquivoDeLivros:
        livrosCad = arquivoDeLivros.read()
    print(livrosCad)

@dataclass
class Livros:
    nome: str
    autor: str
    categoria: str
    preco: float

QUANTIDADE_LIVROS = 1

livros = []

for i in range(QUANTIDADE_LIVROS):
    livro = Livros(
        nome = input("Digite o nome do livro: "),
        autor = input("Digite o nome do autor: "),
        categoria = input("Digite a categoria do livro: "),
        preco = float(input("Digite o preço do livro: "))
    )
    livros.append(livro)
    os.system("clear")

arquivo = "Catálogo_Livros.txt"

with open(arquivo, 'w') as arquivoDeLivros:
    for livro in livros:
        arquivoDeLivros.write(f"Nome: {livro.nome}, Autor: {livro.autor}, Categoria: {livro.categoria}, Preço: {livro.preco} \n")

print("Dados do livro foram salvos!")

ler_dados_catalogo()