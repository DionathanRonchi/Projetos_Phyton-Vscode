from config import DB_CONFIG
import mysql.connector


def cadastrar(nome, preco, quantidade, categoria):
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


def listar():
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


def buscar(termo):
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


def excluir(id_produto):
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
