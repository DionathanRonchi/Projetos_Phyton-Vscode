﻿import sys
from pathlib import Path
import mysql.connector

sys.path.append(str(Path(__file__).resolve().parent.parent))
from BancoDeDados_Integ_Python.produtos.config import DB_CONFIG


def conectar():
    return mysql.connector.connect(**DB_CONFIG)


def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(100),
            telefone VARCHAR(20)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()


def cadastrar_cliente(nome, email=None, telefone=None):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)", (nome, email, telefone))
    conn.commit()
    print(f"Cliente '{nome}' cadastrado.")
    cursor.close()
    conn.close()


def listar_clientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes ORDER BY nome")
    clientes = cursor.fetchall()
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for c in clientes:
            print(f"{c[0]} | {c[1]} | {c[2] if c[2] is not None else '-'} | {c[3] if c[3] is not None else '-'}")
    cursor.close()
    conn.close()


def buscar_cliente(termo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes WHERE nome LIKE %s ORDER BY nome", (f"%{termo}%",))
    clientes = cursor.fetchall()
    if not clientes:
        print("Nenhum cliente encontrado.")
    else:
        for c in clientes:
            print(f"{c[0]} | {c[1]} | {c[2] if c[2] is not None else '-'} | {c[3] if c[3] is not None else '-'}")
    cursor.close()
    conn.close()


def atualizar_email_cliente(id_cliente, novo_email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE clientes SET email = %s WHERE id = %s", (novo_email, id_cliente))
    conn.commit()
    if cursor.rowcount > 0:
        print("E-mail atualizado com sucesso.")
    else:
        print(f"Cliente com id {id_cliente} não encontrado.")
    cursor.close()
    conn.close()


def excluir_cliente(id_cliente):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nome FROM clientes WHERE id = %s", (id_cliente,))
    cliente = cursor.fetchone()
    if not cliente:
        print(f"Cliente com id {id_cliente} não encontrado.")
    else:
        cursor.execute("DELETE FROM clientes WHERE id = %s", (id_cliente,))
        conn.commit()
        print(f"Cliente '{cliente[0]}' removido com sucesso.")
    cursor.close()
    conn.close()


def menu():
    criar_tabela()
    while True:
        print("\n===== SISTEMA DE CLIENTES =====")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Buscar cliente")
        print("4 - Atualizar e-mail")
        print("5 - Excluir cliente")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email (opcional): ") or None
            telefone = input("Telefone (opcional): ") or None
            cadastrar_cliente(nome, email, telefone)
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            termo = input("Buscar por nome: ")
            buscar_cliente(termo)
        elif opcao == "4":
            id_cliente = int(input("ID do cliente: "))
            novo_email = input("Novo e-mail: ") or None
            atualizar_email_cliente(id_cliente, novo_email)
        elif opcao == "5":
            id_cliente = int(input("ID do cliente: "))
            excluir_cliente(id_cliente)
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")


menu()
