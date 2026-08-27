from flask import Flask

# CRIAR A APLICAÇAO FLASK
app = Flask(__name__)

# DEFINE UMA ROTA
@app.route('/')
def index():
    return "Olá! Minha loja OK."

@app.route('/sobre')
def sobre():
    return "Esta é a página sobre a minha loja!!."


@app.route("/produto/<int:id>")
def produto(id):
    return f"Exibindo produto com ID {id}."

@app.route("/produtos")
def produtos():
    return f"1. Notebook - R$ 3.500,00\n2. Smartphone - R$ 1.800,00\n3. Fone de ouvido - R$ 150,00"


#INICIAR SERVIDOR FLASK
if __name__ == '__main__':
    app.run(debug=True)