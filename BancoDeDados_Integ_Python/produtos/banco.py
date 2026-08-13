import mysql.connector
from config import DB_CONFIG


def conectar():
    """Cria e retorna uma conexão com o banco de dados."""
    return mysql.connector.connect(**DB_CONFIG)


def criar_tabelas():
    """Cria a tabela de produtos se não existir."""
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco DECIMAL(10,2) NOT NULL,
            quantidade INT,
            categoria VARCHAR(50)
        )
    """)
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Tabela de produtos criada com sucesso!")
