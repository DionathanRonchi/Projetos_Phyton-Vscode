from flask import Flask, render_template

from agendamentos import buscar_agendamento, listarPorStatus, listar_agendamentos


app = Flask(__name__)


@app.route('/')
def index():
	agendamentos = listar_agendamentos()
	return render_template('index.html', nome_barbearia='DHA - Barbearia', agendamentos=agendamentos)


@app.route('/agendamentos')
def agendamentos():
	return render_template('agendamentos.html', agendamentos=listar_agendamentos())


@app.route('/agendamentos/status/<status>')
def agendamentos_por_status(status):
	return render_template(
		'agendamentos.html',
		agendamentos=listarPorStatus(status),
		status_atual=status,
	)


@app.route('/agendamento/<int:id>')
def detalhe(id):
	resultados = buscar_agendamento(id)
	agendamento = resultados[0] if resultados else None
	return render_template('detalhes.html', agendamento=agendamento)


if __name__ == '__main__':
	app.run(debug=True)
