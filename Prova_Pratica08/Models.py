class item:
    def __init__(self, nome, preco, tipo, disponivel):
        self.nome = nome
        self.preco = preco
        self.tipo = tipo
        self.disponivel = disponivel

    def exibir_informacoes(self):
            print(f"Nome: {self.nome}") 
            print(f"preco: {self.preco}") 
            print(f"tipo {self.tipo}") 
            print(f"disponivel {self.disponivel}")

        
    def converte_tupla(self):
            return (self.nome, self.preco, self.tipo, self.disponivel)

    @staticmethod
    def reverte_tupla(tupla):
                i = item(
                    nome = tupla[1],
                    preco = tupla[2],
                    tipo = tupla[3],
                    disponivel= tupla[4]
                )
        
                i.id = tupla[0]
                return i
        
i1 = item("Garfo", "10,00", "Cozinha", "Disponivel: 5")
i2 = item("Teclado", "100,00", "Tecnologia", "Disponivel: 50")
        
i1.exibir_informacoes()
print()
i2.exibir_informacoes()

