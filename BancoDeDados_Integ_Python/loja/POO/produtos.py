import mysql.connector
from .config import DB_CONFIG
from .models import produto

def cadastrar_produto(produto: produto):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO produtos (nome, preco, quantidade, categoria) VALUES (%s, %s, %s, %s)",
            produto.converte_tupla()
        )
        conexao.commit()
        print(f"Produto {produto.nome} cadastrado com sucesso!")
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
        cursor.execute("SELECT * FROM produtos ORDER BY id")
        return [produto.revert_tupla(linha) for linha in cursor.fetchall()]
    except mysql.connector.Error as erro:
        print(f"Erro ao listar produtos: {erro}")
        return []
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def buscar_produto(termo: str):
    """Busca produtos por nome parcial"""
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produtos WHERE nome LIKE %s", (f"%{termo}%",))
        return [produto.revert_tupla(linha) for linha in cursor.fetchall()]
    except mysql.connector.Error as erro:
        print(f"Erro ao buscar produtos: {erro}")
        return []
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def busca_produto_por_id(id: int):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produtos WHERE id = %s", (id,))
        resultado = cursor.fetchone()
        if resultado:
            return produto.revert_tupla(resultado)
        return None
    except mysql.connector.Error as erro:
        print(f"Erro ao buscar produto: {erro}")
        return None
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
        result = cursor.fetchone()
        if not result:
            print(f"Produto com id {id_produto} não encontrado.")
            return
        cursor.execute("DELETE FROM produtos WHERE id = %s", (id_produto,))
        conexao.commit()
        print(f"Produto '{result[0]}' excluído com sucesso.")
    except mysql.connector.Error as erro:
        print(f"Erro ao excluir: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()            