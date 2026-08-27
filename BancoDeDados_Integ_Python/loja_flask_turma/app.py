from flask import Flask, render_template

# CRIAR A APLICAÇAO FLASK
app = Flask(__name__)

# DEFINE UMA ROTA
@app.route('/')
def index():
     return render_template('index.html')

@app.route("/produtos")
def produtos():
    return render_template('produtos.html')


@app.route('/sobre')
def sobre():
    return "Esta é a página sobre."

@app.route("/produto/<int:id>")
def produto(id):
    return f"Exibindo produto com ID {id}."


@app.route("/categoria/<nome>")
def categoria(nome):
    return f"Produtos da categoria: {nome}."

#INICIAR SERVIDOR FLASK
if __name__ == '__main__':
    app.run(debug=True)