import mysql
from mysql.connector import Error

# Estabelecendo conexão com o banco de dados
def create_connection():
    return mysql.connector.connect(
        host='localhost',  # Endereço do servidor
        user='root',       # Usuário do banco de dados
        password='mysql',   # Senha do banco de dados
        database='star_wars_db'  # Nome do banco de dados
    )

# Função para executar comandos SQL
def execute_query(conexao, comando):
    cursor = conexao.cursor()
    try:
        cursor.execute(comando)
        conexao.commit()
    except Error as e:
        print(f"Erro ao executar o comando: {e}")
    finally:
        cursor.close()

# Função para buscar todos os resultados de uma consulta
def fetch_all(conexao, comando):
    cursor = conexao.cursor()
    try:
        cursor.execute(comando)
        return cursor.fetchall()
    except Error as e:
        print(f"Erro ao buscar resultados: {e}")
        return []
    finally:
        cursor.close()

# Função para buscar apenas um resultado de uma consulta
def fetch_one(conexao, comando):
    cursor = conexao.cursor()
    try:
        cursor.execute(comando)
        return cursor.fetchone()
    except Error as e:
        print(f"Erro ao buscar resultado: {e}")
        return None
    finally:
        cursor.close()
