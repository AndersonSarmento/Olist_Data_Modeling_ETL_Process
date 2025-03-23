import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
from db_utils import fetch_all

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Estabelecendo conexão com o banco de dados
def create_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),       # Endereço do servidor
        user=os.getenv("DB_USER"),       # Usuário do banco de dados
        password=os.getenv("DB_PASSWORD"),  # Senha do banco de dados
        database=os.getenv("DB_NAME")    # Nome do banco de dados
    )

if __name__ == "__main__":
    try:
        # Estabelecendo conexão com o banco de dados
        conexao = create_connection()

        # Exemplo de consulta na tabela 'personagens'
        personagens = fetch_all(conexao, "SELECT * FROM personagens")
        print("Personagens:", personagens)
    except Error as e:
        print(f"Erro ao conectar ou executar consulta: {e}")
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()