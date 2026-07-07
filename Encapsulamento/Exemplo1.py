class Cofre:
    def __init__(self, dono):
        self.dono = dono
        self.__valor = 0

    # GETTER
    def get_valor(self):
        return self.__valor

    # MÉTODOS
    def depositar(self, valor):
        if valor > 0:
            self.__valor += valor
        else:
            print("Valor de depósito inválido. Insira um valor positivo.")

    def retirar(self, valor):
        if valor <= 0:
            print("Valor de retirada inválido. Insira um valor positivo.")
        elif valor > self.__valor:
            print("Saldo insuficiente para essa retirada.")
        else:
            self.__valor -= valor

    def exibir_saldo(self):
        print("=" * 30)
        print(f"Dono: {self.dono}")
        print(f"Saldo: R$ {self.__valor:.2f}")
        print("=" * 30)


if __name__ == "__main__":
    c1 = Cofre(dono="Ana")
    c1.depositar(500)
    c1.depositar(-100)
    c1.retirar(200)
    c1.retirar(1000)
    c1.exibir_saldo()

    c2 = Cofre(dono="Bruno")
    c2.depositar(1000)
    c2.retirar(300)
    c2.exibir_saldo()