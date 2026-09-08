import mysql.connector

from BancoDeDados_Integ_Python.lanchonete.config import DB_CONFIG
def conectar():
    return mysql.connector.connect(**DB_CONFIG)

