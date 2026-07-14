#CLASSE PAI
class conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

    def exibir_saldo(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: R$ {self.saldo:.2f}")
        print("-"*20)


#CLASSE FILHA
class ContaPoupanca(conta):
    def __init__(self, titular, saldo, taxa_rendimento):
        super().__init__(titular, saldo)
        self.taxa_rendimento = taxa_rendimento

    def render(self):
        self.saldo = self.saldo * (1 + self.taxa_rendimento)
        print(f"Rendimento aplicado! Novo saldo: R$ {self.saldo:.2f}")


class ContaCorrente(conta):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite

    def depositar(self, valor):
        if valor < 0:
            print("Operação inválida: depósito não pode ser negativo.")
            return
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if valor > self.saldo + self.limite:
            print("Saque não permitido: valor excede saldo + limite.")
            return
        self.saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")


#USO
c = conta("Ana", 1000)
p = ContaPoupanca("Maria", 1000, 0.02)
cc = ContaCorrente("João", 800, 300)

c.exibir_saldo()

p.exibir_saldo()
p.depositar(500)
p.render()
p.exibir_saldo()

cc.exibir_saldo()
cc.depositar(200)
cc.depositar(-100)
cc.sacar(1000)
cc.exibir_saldo()
cc.sacar(500)