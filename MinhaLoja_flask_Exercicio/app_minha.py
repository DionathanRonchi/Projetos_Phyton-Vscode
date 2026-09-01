from flask import Flask, render_template

# CRIAR A APLICAÇAO FLASK
app = Flask(__name__)

lista = [
       {"id": 1, "nome": "Teclado", "preco": 500.00, "categoria": "Eletronicos", "qualidade": "10"},
       {"id": 2, "nome": "Colher", "preco": 30.50, "categoria": "Cozinha", "qualidade": "0"},
       {"id": 3, "nome": "Condicionador", "preco": 7.99, "categoria": "Banheiro", "qualidade": "8"},
       {"id": 4, "nome": "Camiseta", "preco": 50.00, "categoria": "Vestuário", "qualidade": "9"},
       {"id": 5, "nome": "Cadeira", "preco": 150.00, "categoria": "Móveis", "qualidade": "7"},
       {"id": 6, "nome": "Mouse", "preco": 100.00, "categoria": "Eletronicos", "qualidade": "0"}
       ]

# DEFINE UMA ROTA
@app.route('/')
def index():
    return render_template('index_minha.html')


@app.route('/sobre')
def sobre():
    return render_template('sobre_minha.html')


@app.route("/produto/<int:id>")
def detalhes_produto(id):
    produto = None
    for p in lista:
        if p["id"] == id:
            produto = p
            break
    return render_template('detalhes.html', id=id, produto=produto)


@app.route("/produtos")
def produtos():
    return render_template('produtos_minha.html', produtos=lista)


@app.route("/catalogo")
def catalogo():
   return render_template('catalogo_minha.html', produtos=lista)


@app.route("/categoria/produtos/<string:categoria>")
def categoria(categoria):
    produtos_filtrados = [produto for produto in lista if produto["categoria"] == categoria]
    return render_template('produtos_minha.html', produtos=produtos_filtrados)


#INICIAR SERVIDOR FLASK
if __name__ == '__main__':
    app.run(debug=True)