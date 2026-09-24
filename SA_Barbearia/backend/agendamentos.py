import mysql.connector          #importando o mysql
from banco import conectar
from models import Agendamento

# def cadastrar_agendamento(agendamento: Agendamento): #cadastrando agendamento
#
#    conexao = None
#    try: 
#        conexao = conectar()
#        cursor = conexao.cursor()
#        cursor.execute(
#            "INSERT INTO agendamentos (cliente, telefone, servico, preco, barbeiro, data, horario, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
#            agendamento.converte_tupla()
#        )
#        conexao.commit()
#        print(f"Agendamento do cliente '{agendamento.cliente}' cadastrado.")
#    except mysql.connector.Error as erro:
#        print(f"Erro ao cadastrar: {erro}")
#    finally:
#        if conexao and conexao.is_connected():
#            conexao.close()

def listar_agendamentos():             # listar agendamentos

    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM agendamentos ORDER BY data, horario")
        return [Agendamento.reverte_tupla(linha) for linha in cursor.fetchall()]
    except mysql.connector.Error as erro:
        print(f"Erro ao listar: {erro}")
        return []
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def listarPorStatus(status):             # listar agendamentos por status

    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM agendamentos WHERE status = %s ORDER BY data, horario", (status,))
        return [Agendamento.reverte_tupla(linha) for linha in cursor.fetchall()]
    except mysql.connector.Error as erro:
        print(f"Erro ao listar: {erro}")
        return []
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def buscar_agendamento(termo):             # buscar agendamentos
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT * FROM agendamentos WHERE id = %s", 
        (termo,)
        )
        return [Agendamento.reverte_tupla(linha) for linha in cursor.fetchall()]
    except mysql.connector.Error as erro:
        print(f"Erro ao buscar: {erro}")
        return []
    finally:
        if conexao and conexao.is_connected():
            conexao.close()