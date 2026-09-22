# banco.py
# Responsável por criar a conexão com o banco de dados.

import mysql.connector
from config import DB_CONFIG


def conectar():
    try:
        return mysql.connector.connect(**DB_CONFIG)

    except mysql.connector.Error as erro:
        print("Erro ao conectar:", erro)
        return None