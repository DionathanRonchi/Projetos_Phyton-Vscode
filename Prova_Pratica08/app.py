from flask import Flask, render_template

# CRIAR A APLICAÇAO FLASK
app = Flask(__name__)


# DEFINE UMA ROTA
@app.route('/')
def index():
    return render_template('KingBurguer.html')

@app.route("/lanchonete/<int:id>")
def detalhes_lanchonete(id):
    produto = None
    for l in lista:
        if p["id"] == id:
            detalhes_lanchonete = l
            break
    return render_template('detalhes.html', id=id, lanchonete  = lanchonete)