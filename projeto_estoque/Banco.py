
import psycopg2
from flask import Flask

app = Flask(__name__)

DATABASE_URL = "postgresql://postgres:GfNetsUGDSLmcrevlDTXKfKatziHNoCo@junction.proxy.rlwy.net:23638/railway"  # Substitua pela URL do Railway

def connect_db():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    except Exception as e:
        print("Erro ao conectar ao banco:", e)
        return None

@app.route('/')
def home():
    conn = connect_db()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT 'Conexão bem-sucedida!'")
        result = cur.fetchone()
        cur.close()
        conn.close()
        return result[0]
    return "Erro ao conectar ao banco de dados."

if __name__ == '__main__':
    app.run(debug=True)
    