class Cofre:
    def __init__(self, dono):
        self.dono = dono
        self.__valor = 0
 
    def depositar(self, valor):
        if valor > 0:
            self.__valor += valor
            print(f"[Cofre de {self.dono}] Depósito: R$ {valor:.2f} - Novo saldo: R$ {self.__valor:.2f}")
        else:
            print(f"[Cofre de {self.dono}] Valor inválido para depósito: {valor}")
 
    def retirar(self, valor):
        if valor <= 0:
            print(f"[Cofre de {self.dono}] Valor inválido para retirada: {valor}")
        elif valor > self.__valor:
            print(f"[Cofre de {self.dono}] Saldo insuficiente para retirar {valor}")
        else:
            self.__valor -= valor
 
    def get_valor(self):
        return self.__valor
 
    def exibir_saldo(self):
        print(f"Cofre de {self.dono} - Saldo: R$ {self.__valor:.2f}")