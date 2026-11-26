from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__, static_folder='.', static_url_path='')
def criar_banco():
    conn = sqlite3.connect('contatos.db')
    conn.execute('CREATE TABLE IF NOT EXISTS contatos (id INTEGER PRIMARY KEY, nome TEXT, email TEXT, mensagem TEXT)')
    conn.close()

criar_banco()

@app.route('/')
def home():
    return render_template('Homepage.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nome = request.form['nome']
    email = request.form['email']
    mensagem = request.form['mensagem']

    conn = sqlite3.connect('contatos.db')
    conn.execute('INSERT INTO contatos (nome, email, mensagem) VALUES (?, ?, ?)', (nome, email, mensagem))
    conn.commit()
    conn.close()
    return redirect('/#contato')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)