class Agendamento:
    def __init__(self, cliente, telefone, servico, preco, barbeiro, data, horario, status, id=None):
        self.id = id
        self.cliente = cliente
        self.telefone = telefone
        self.servico = servico
        self.preco = preco
        self.barbeiro = barbeiro
        self.data = data
        self.horario = horario
        self.status = status
    
    def exibir(self):
        print(f"Cliente: {self.cliente} | Telefone: {self.telefone} | Serviço: {self.servico} | Preço: R${self.preco:.2f} | Barbeiro: {self.barbeiro} | Data: {self.data} | Horário: {self.horario} | Status: {self.status}")

    def converte_tupla(self):
        return (self.cliente, self.telefone, self.servico, self.preco, self.barbeiro, self.data, self.horario, self.status)

    @staticmethod   #metodo que pertence a classe mas não depende de nenhum objeto
    def reverte_tupla(tupla):
        agendamento = Agendamento(
            id = tupla[0],
            cliente = tupla[1],
            telefone = tupla[2],
            servico = tupla[3],
            preco = float(tupla[4]) if tupla[4] is not None else 0,
            barbeiro = tupla[5],
            data = tupla[6],
            horario = tupla[7],
            status = tupla[8]
        )
        return agendamento

    