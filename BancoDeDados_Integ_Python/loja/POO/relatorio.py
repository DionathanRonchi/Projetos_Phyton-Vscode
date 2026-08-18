from .config import DB_CONFIG
import mysql.connector


def total_produtos():
    """Retorna o total de produtos cadastrados."""
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("SELECT COUNT(*) FROM produtos")
        total = cursor.fetchone()[0]
        print(f"Total de produtos: {total}")
        return total
    except mysql.connector.Error as erro:
        print(f"Erro ao contar produtos: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()


def valor_total_estoque():
    """Calcula e retorna o valor total do estoque (preco * quantidade)."""
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("SELECT SUM(preco * quantidade) FROM produtos")
        total = cursor.fetchone()[0]
        if total is None:
            total = 0
        print(f"Valor total do estoque: R${total:.2f}")
        return total
    except mysql.connector.Error as erro:
        print(f"Erro ao calcular valor total: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()


def produto_mais_caro():
    """Retorna o produto mais caro cadastrado."""
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produtos ORDER BY preco DESC LIMIT 1")
        produto = cursor.fetchone()
        if produto:
            print(f"Produto mais caro: {produto[1]} - R${produto[2]:.2f}")
            return produto
        else:
            print("Nenhum produto cadastrado.")
            return None
    except mysql.connector.Error as erro:
        print(f"Erro ao buscar produto mais caro: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()
