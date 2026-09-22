# models.py
# Classe responsável por representar os itens do cardápio.

class pet:

    def __init__(self, nome, especie, dono):
        self.nome = nome
        self.preco = especie
        self.tipo = dono

    def exibir(self):
        print(f"{self.nome} - {self.especie} - {self.dono}")

    def converte_tuple(self):
        return (self.nome, self.especie, self.dono)

    @staticmethod
    def reverte_tuple(tupla):
        id, nome, especie, dono, = tupla
        pet = pet(nome, especie, dono)
        pet.id = id
        return pet

pet1 = pet("Bob", "Cachorro", "João")
pet2 = pet("Docinho", "Gato", "Robson")

pet1.exibir()
pet2.exibir()

pet3 = pet.reverte_tuple(("Robert", "Calopsita", "Cleyton"))
pet3.exibir()