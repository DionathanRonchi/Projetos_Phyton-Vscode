from . import banco
from . import produtos
from . import relatorio
from .models import produto

def exibir_lista(lista):
    if lista:
        for item in lista:
            item.exibir()
    else:
        print("Nenhum produto encontrado.")                

def menu():
    while True:
        print("\n=== Menu ===")
        print("1. Cadastrar Produto")
        print("2. Listar Produtos")
        print("3. Buscar Relatório")
        print("4. Atualizar preço")
        print("5. Excluir produto")
        print("0. Sair")

        opcao = input("opção: ")

        if opcao == "1":
            nome = input("Nome:")
            preco = float(input("Preço: "))
            qtd = int(input("Quantidade: "))
            cat = input("Categoria: ")

            novo_produto = produto(nome, preco, qtd, cat)
            produtos.cadastrar_produto(novo_produto)

        elif opcao == "2":
            exibir_lista(produtos.listar_produtos())

        elif opcao == "3":
            termo = input("Buscar nome: ")    
            exibir_lista(produtos.buscar_produto(termo))

        elif opcao == "4":
            pid = int(input("ID do produto: "))
            novo = float(input("Novo preço: "))
            produtos.atualizar_preco(pid, novo)

        elif opcao == "5":
            pid = int(input("ID do produto: "))
            produtos.excluir_produto(pid)    

        elif opcao == "0":
            print("Saindo...")
            break


if __name__ == "__main__":
    menu()    