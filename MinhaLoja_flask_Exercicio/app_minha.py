from flask import Flask, render_template

# CRIAR A APLICAÇAO FLASK
app = Flask(__name__)

# DEFINE UMA ROTA
@app.route('/')
def index():
    return render_template('index_minha.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre_minha.html')


@app.route("/produto/<int:id>")
def produto(id):
    return render_template('produto_minha.html', id=id)


@app.route("/produtos")
def produtos():
   lista = [
       {"id": 1, "nome": "Teclado", "preco": 500.00, "categoria": "Eletronicos"},
       {"id": 2, "nome": "Colher", "preco": 30.50, "categoria": "Cozinha"},
       {"id": 3, "nome": "Condicionador", "preco": 7.99, "categoria": "Banheiro"},
       {"id": 4, "nome": "Camiseta", "preco": 50.00, "categoria": "Vestuário"},
       {"id": 5, "nome": "Cadeira", "preco": 150.00, "categoria": "Móveis"}
       ]
   return render_template('produtos_minha.html', produtos=lista)

#INICIAR SERVIDOR FLASK
if __name__ == '__main__':
    app.run(debug=True)