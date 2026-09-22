# models.py
# Classe responsável por representar os itens do cardápio.

class Item:

    def __init__(self, nome, preco, tipo, disponivel):
        self.nome = nome
        self.preco = preco
        self.tipo = tipo
        self.disponivel = disponivel

    def exibir(self):
        status = "Disponível" if self.disponivel else "Esgotado"
        print(f"{self.nome} - R$ {self.preco:.2f} - {self.tipo} - {status}")

    def converte_tuple(self):
        return (self.nome, self.preco, self.tipo, self.disponivel)

    @staticmethod
    def reverte_tuple(tupla):
        id, nome, preco, tipo, disponivel = tupla
        item = Item(nome, preco, tipo, disponivel)
        item.id = id
        return item


item1 = Item("Hambúrguer", 18.90, "Lanche", True)
item2 = Item("Coca-Cola", 6.00, "Bebida", True)

item1.exibir()
item2.exibir()

item3 = Item.reverte_tuple((9, "Milkshake de Creme", 14.90, "Bebida", False))
item3.exibir()