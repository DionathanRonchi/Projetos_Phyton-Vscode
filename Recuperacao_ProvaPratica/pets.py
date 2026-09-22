# Funções responsáveis por cadastrar, listar e buscar os pets.

from banco import conectar
from models import Item


def cadastrar_pet(pet):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        sql = """
        INSERT INTO pets
        (nome, especie, dono)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(sql, pet.converte_tuple())
        conexao.commit()

        pet.id = cursor.lastrowid

    except Exception as erro:
        print("Erro ao cadastrar:", erro)

    finally:
        if conexao:
            conexao.close()


def listar_pets():
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM pets")

        dados = cursor.fetchall()

        return [pet.reverte_tuple(pet) for pet in dados]

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
            "SELECT * FROM pets WHERE id = %s",
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