class ContaBancaria:

    def __init__(self, titular, numero, saldo_inicial=0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo_inicial

    # Depositar
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Deposito de R$ {valor:.2f} realizado com sucesso")
        else:
            print("Valor de deposito invalido")

    # Sacar
    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque invalido")
        elif valor > self.saldo:
            print("Saldo Insuficiente")
        else:
            self.saldo -= valor
            print(f"Saque no valor de R$ {valor:.2f} realizado com sucesso")

    # Exibir extrato
    def exibir_extrato(self):
        print("=" * 20)
        print(f"Conta: {self.numero}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: R$ {self.saldo:.2f}")
        print("=" * 20)


# Uso da classe (fora da classe, sem indentação)
conta1 = ContaBancaria(titular="Conta 1", numero=1, saldo_inicial=0)
conta1.depositar(300.00)
conta1.sacar(300.00)
conta1.exibir_extrato()