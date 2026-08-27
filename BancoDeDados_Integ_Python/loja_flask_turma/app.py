from flask import Flask, render_template

# CRIAR A APLICAÇAO FLASK
app = Flask(__name__)

# DEFINE UMA ROTA
@app.route('/')
def index():
     return render_template('index.html')

@app.route("/produtos")
def produtos():
    lista = [
        {"nome": "Notebook", "preco": 3499.00, "categoria": "Eletronicos"},
        {"nome": "Frigideira", "preco": 30.50, "categoria": "Cozinha"},
        {"nome": "Shampoo", "preco": 7.99, "categoria": "Banheiro"}
    ]
    return render_template('produtos.html', produtos=lista)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route("/produto/<int:id>")
def produto(id):
    return f"Exibindo produto com ID {id}."


@app.route("/categoria/<nome>")
def categoria(nome):
    return render_template('categoria.html', nome=nome, produtos=[])  

#INICIAR SERVIDOR FLASK
if __name__ == '__main__':
    app.run(debug=True)