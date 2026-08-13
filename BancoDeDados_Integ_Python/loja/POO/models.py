class produto:
    def __init__(self, nome, preco, quantidade, categoria):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.categoria = categoria

    def converte_tupla(self):
        return (self.nome, self.preco, self.quantidade, self.categoria)

    @staticmethod
    def revert_tupla(self, tupla):
        produto = produto(
           nome = tupla[1], 
           preco = tupla[2], 
           quantidade = tupla[3], 
           categoria = tupla[4]
           )
        
        produto = id = tupla[0]
        return produto

    def exibir(self):
        print(f"{self.id} | {self.nome} | {self.preco} | {self.quantidade} | {self.categoria}")