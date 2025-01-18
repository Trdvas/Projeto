import tkinter as tk
from tkinter import messagebox
import psycopg2

# Conexão com o PostgreSQL
conexao = psycopg2.connect(
    dbname="Projeto_estoque",
    user="postgres",
    password="P3F1c4f1452369",
    host="localhost",
    port="5432"
)
cursor = conexao.cursor()

# Função para adicionar usuário
def adicionar_usuario():
    nome = entry_nome.get()
    email = entry_email.get()
    senha = entry_senha.get()

    if nome and email and senha:
        try:
            cursor.execute(
                "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)",
                (nome, email, senha)
            )
            conexao.commit()
            messagebox.showinfo("Sucesso", "Usuário adicionado com sucesso!")
            entry_nome.delete(0, tk.END)
            entry_email.delete(0, tk.END)
            entry_senha.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao adicionar usuário: {e}")
    else:
        messagebox.showwarning("Aviso", "Preencha todos os campos!")

# Interface gráfica com Tkinter
app = tk.Tk()
app.title("Cadastro de Usuários")

tk.Label(app, text="Nome:").grid(row=0, column=0)
entry_nome = tk.Entry(app)
entry_nome.grid(row=0, column=1)

tk.Label(app, text="Email:").grid(row=1, column=0)
entry_email = tk.Entry(app)
entry_email.grid(row=1, column=1)

tk.Label(app, text="Senha:").grid(row=2, column=0)
entry_senha = tk.Entry(app, show="*")
entry_senha.grid(row=2, column=1)

btn_adicionar = tk.Button(app, text="Adicionar Usuário", command=adicionar_usuario)
btn_adicionar.grid(row=3, columnspan=2)

app.mainloop()

# Fechar a conexão ao encerrar o programa
cursor.close()
conexao.close()
