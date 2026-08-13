from BancoDeDados_Integ_Python.produtos.config import DB_CONFIG
import mysql.connector

conexao = None

try:
    conexao = mysql.connector.connect(**DB_CONFIG)
    cursor = conexao.cursor()

    cursor.execute("""
        create table if not exists produtos (
        id int auto_increment primary key,
        nome varchar(100) not null,
        preco decimal(10,2) not null,
        quantidade int,
        categoria varchar(50))
    """)
    conexao.commit()
    print("Tabela criada com sucesso!")

except mysql.connector.Error as erro:
    print(f"Erro: {erro}")

finally:
    if conexao and conexao.is_connected():
        conexao.close()


def cadastrar_produto(nome, preco, quantidade, categoria):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO produtos (nome, preco, quantidade, categoria) VALUES (%s, %s, %s, %s)",
            (nome, preco, quantidade, categoria)
        )
        conexao.commit()
        print(f"Produto '{nome}' cadastrado.")
    except mysql.connector.Error as erro:
        print(f"Erro ao cadastrar: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def listar_produtos():
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produtos ORDER BY nome")
        for p in cursor.fetchall():
            print(f"{p[0]} | {p[1]} | R${p[2]:.2f} | Qtd: {p[3]} | {p[4]}")
    except mysql.connector.Error as erro:
        print(f"Erro ao listar: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def buscar_produto(termo):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT * FROM produtos WHERE nome LIKE %s ORDER BY nome",
            (f"%{termo}%",)
        )
        for p in cursor.fetchall():
            print(f"{p[0]} | {p[1]} | R${float(p[2]):.2f} | Qtd: {p[3]} | {p[4]}")
    except mysql.connector.Error as erro:
        print(f"Erro ao buscar: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def atualizar_preco(id_produto, novo_preco):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute(
            "UPDATE produtos SET preco = %s WHERE id = %s",
            (novo_preco, id_produto)
        )
        conexao.commit()
        if cursor.rowcount > 0:
            print("Preço atualizado com sucesso.")
        else:
            print(f"Produto com id {id_produto} não encontrado.")
    except mysql.connector.Error as erro:
        print(f"Erro ao atualizar: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def excluir_produto(id_produto):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("SELECT nome FROM produtos WHERE id = %s", (id_produto,))
        produto = cursor.fetchone()
        if not produto:
            print(f"Produto com id {id_produto} não encontrado.")
            return
        cursor.execute("DELETE FROM produtos WHERE id = %s", (id_produto,))
        conexao.commit()
        print(f"Produto '{produto[0]}' excluído com sucesso.")
    except mysql.connector.Error as erro:
        print(f"Erro ao excluir: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()


# --- Uso ---
def menu():
    while True:
        print("\n===== SISTEMA DE PRODUTOS =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Buscar produto")
        print("4 - Atualizar preço")
        print("5 - Excluir produto")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            preco = float(input("Preço: "))
            qtd = int(input("Quantidade: "))
            cat = input("Categoria: ")
            cadastrar_produto(nome, preco, qtd, cat)
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            termo = input("Buscar por nome: ")
            buscar_produto(termo)
        elif opcao == "4":
            pid = int(input("ID do produto: "))
            novo = float(input("Novo preço: "))
            atualizar_preco(pid, novo)
        elif opcao == "5":
            pid = int(input("ID do produto: "))
            excluir_produto(pid)
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

#--- Chamado das funções ---
#criar_tabela()          #executar uma unica vez

menu()                   #executa de modo recorrente