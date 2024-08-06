from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

@app.route("/inicio")
def home():
    df = pd.read_csv("tabela - livros.csv")
    #lista = df["Titulo do Livro"].tolist()
    lista_de_livros = []
    for index, row in df.iterrows():
        livro = Livro(row["Titulo do Livro"],row["Autor"],row["Categoria"],row["Ano de Publicação"])
        lista_de_livros.append(livro)
    return render_template("lista.html", titulo="Listagem de Livros - SENAI", lista_de_livros=lista_de_livros)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Livro')

class Livro:
    def __init__(self,titulo,autor,categoria,ano,editora='Sem Editora'):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.ano = ano
        self.editora = editora
        self.ativo = False

#lista de livros inicial
livro1 = Livro('1984','George Orwell','Ficção',1949)
livro2 = Livro('O Senhor dos Aneis','J.R.R. Tolkien','Fantasia',1954)
livro3 = Livro('Don Casmurro','Machado de Assis','Romance',1899)
lista = [livro1,livro2,livro3]



@app.route('/criar', methods=['POST'])
def criar():
    titulo = request.form['titulo']
    autor = request.form['autor']
    categoria = request.form['categoria']
    ano = request.form['ano']
    editora = request.form['editora']
    livro = Livro(titulo,autor,categoria,ano,editora)
    lista.append(livro)
    return render_template('lista.html',titulo='Livros',livros = lista)

if __name__ == "__main__":
    app.run()