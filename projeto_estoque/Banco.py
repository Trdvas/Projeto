
import psycopg2

try:
    conexao = psycopg2.connect(
        dbname="Projeto_estoque",
        user="postgres",
        password="P3F1c4f1452369",
        host="localhost",
        port="5432"
    )
    cursor = conexao.cursor()
    print("Conexão com o banco bem-sucedida!")
except Exception as e:
    print("Erro ao conectar ao banco:", e)
    