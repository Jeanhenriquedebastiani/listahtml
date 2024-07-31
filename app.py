from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)

@app.route("/lista")
def lista_livros():
    df = pd.read_csv("tabela - livros.csv")
    lista = df["Titulo do Livro"].tolist()
    return render_template("lista.html", titulo="Listagem de Livros - SENAI", lista_de_livros=lista)


app.run(debug=True)