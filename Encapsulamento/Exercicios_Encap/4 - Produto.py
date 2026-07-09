class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.__estoque = 0

    # GETTER
    def get_estoque(self):
        return self.__estoque

    # MÉTODOS
    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.__estoque += quantidade
        else:
            print("Quantidade inválida para reposição.")

    def vender(self, quantidade):
        if quantidade <= 0:
            print("Quantidade inválida para venda.")
        elif quantidade > self.__estoque:
            print("Estoque insuficiente para essa venda.")
        else:
            self.__estoque -= quantidade

    def exibir_info(self):
        print("=" * 30)
        print(f"Produto: {self.nome}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Estoque: {self.__estoque}")
        print("=" * 30)


if __name__ == "__main__":
    p1 = Produto(nome="Notebook", preco=3500.00)
    p1.adicionar_estoque(10)
    p1.vender(3)
    p1.vender(20)
    p1.exibir_info()

    p2 = Produto(nome="Mouse", preco=79.90)
    p2.adicionar_estoque(50)
    p2.vender(15)
    p2.adicionar_estoque(-5)
    p2.exibir_info()