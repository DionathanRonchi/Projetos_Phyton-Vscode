# cardapio.py
# Funções responsáveis por cadastrar, listar e buscar itens.

from banco import conectar
from models import Item


def cadastrar_item(item):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        sql = """
        INSERT INTO cardapio
        (nome, preco, tipo, disponivel)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(sql, item.converte_tuple())
        conexao.commit()

        item.id = cursor.lastrowid

    except Exception as erro:
        print("Erro ao cadastrar:", erro)

    finally:
        if conexao:
            conexao.close()


def listar_itens():
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM cardapio")

        dados = cursor.fetchall()

        return [Item.reverte_tuple(item) for item in dados]

    except Exception as erro:
        print("Erro ao listar:", erro)
        return []

    finally:
        if conexao:
            conexao.close()


def buscar_por_id(id):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT * FROM cardapio WHERE id = %s",
            (id,)
        )

        resultado = cursor.fetchone()

        if resultado:
            return Item.reverte_tuple(resultado)

        return None

    except Exception as erro:
        print("Erro ao buscar:", erro)
        return None

    finally:
        if conexao:
            conexao.close()