class Cliente:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"E-mail: {self.email}")

    def converte_tupla(self):
        return (self.nome, self.telefone, self.email)

    @staticmethod
    def reverte_tupla(tupla):
        c = Cliente(
            nome = tupla[1],
            telefone = tupla[2],
            email = tupla[3]
        )

        c.id = tupla[0]
        return c

c1 = Cliente("Lucas", "123456789", "lucas@email.com")
c2 = Cliente("Maria", "987654321", "maria@email.com")

c1.exibir_informacoes()
print()
c2.exibir_informacoes()


