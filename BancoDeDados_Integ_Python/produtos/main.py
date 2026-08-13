from config import DB_CONFIG
from banco import conectar, criar_tabelas
from produtos import cadastrar, listar, buscar, atualizar_preco, excluir
from relatorio import total_produtos, valor_total_estoque, produto_mais_caro
import mysql.connector

# Criar tabelas na primeira execução
try:
    criar_tabelas()
except Exception as erro:
    print(f"Erro ao criar tabelas: {erro}")


# --- Menu Principal ---
def menu():
    while True:
        print("\n===== SISTEMA DE PRODUTOS =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Buscar produto")
        print("4 - Atualizar preço")
        print("5 - Excluir produto")
        print("6 - Total de produtos")
        print("7 - Valor total do estoque")
        print("8 - Produto mais caro")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            preco = float(input("Preço: "))
            qtd = int(input("Quantidade: "))
            cat = input("Categoria: ")
            cadastrar(nome, preco, qtd, cat)
        elif opcao == "2":
            listar()
        elif opcao == "3":
            termo = input("Buscar por nome: ")
            buscar(termo)
        elif opcao == "4":
            pid = int(input("ID do produto: "))
            novo = float(input("Novo preço: "))
            atualizar_preco(pid, novo)
        elif opcao == "5":
            pid = int(input("ID do produto: "))
            excluir(pid)
        elif opcao == "6":
            total_produtos()
        elif opcao == "7":
            valor_total_estoque()
        elif opcao == "8":
            produto_mais_caro()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()