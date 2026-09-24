import mysql.connector
from config import DB_CONFIG

def conectar():
    return mysql.connector.connect(**DB_CONFIG)

def criar_tabela():
    conexao = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS agendamentos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                cliente VARCHAR(100) not null, 
                telefone VARCHAR(20),
                servico VARCHAR(100),
                preco DECIMAL(10,2),
                barbeiro VARCHAR(50),
                data DATE not null,
                horario VARCHAR(5),
                status VARCHAR(20) default 'Agendado',
                check (status in ('Agendado', 'Concluído', 'Cancelado'))
                );
        """)
        conexao.commit()
        print("Tabela criada com sucesso!")
    except mysql.connector.Error as erro:
        print(f"Erro: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()