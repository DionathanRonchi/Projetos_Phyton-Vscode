class produto:
    def __init__(self, nome, preco, quantidade, categoria):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.categoria = categoria

    def converte_tupla(self):
        return (self.nome, self.preco, self.quantidade, self.categoria)

    @staticmethod
    def revert_tupla(tupla):
        p = produto(
           nome = tupla[1], 
           preco = tupla[2], 
           quantidade = tupla[3], 
           categoria = tupla[4]
           )
        
        p.id = tupla[0]
        return p

    def exibir(self):
        print(f"{self.id} | {self.nome} | {self.preco} | {self.quantidade} | {self.categoria}")