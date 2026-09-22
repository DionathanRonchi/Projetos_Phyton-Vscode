# app.py
# Aplicação Flask responsável pelas páginas do cardápio.

from flask import Flask, render_template
from pets import listar_itens, buscar_por_id

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/pet")
def pet():
    itens = listar_itens()
    return render_template("pets.html", pets=pet)


@app.route("/pet/<int:id>")
def detalhe(id):
    item = buscar_por_id(id)
    return render_template("detalhe.html", item=item)


if __name__ == "__main__":
    app.run(debug=True)