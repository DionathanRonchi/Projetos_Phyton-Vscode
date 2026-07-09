#PAI
class animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print(f"{self.nome} emite um som.")

    def mover(self):
        print(f"{self.nome} se move.")

    def exibir_info(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print("-"*20)



class Cachorro(animal):
        def __init__(self, nome, idade, raca):
            super().__init__(nome, idade)
            self.raca = raca

        def emitir_som(self):
            print(f"{self.nome} late.")

        def mover(self):
            print(f"{self.nome} corre em 4 patas.")
        
        def exibir_info(self):
            super().exibir_info()
            print(f"Raça: {self.raca}")
            


class Passaro(animal):
        def __init__(self, nome, idade, pode_voar):
            super().__init__(nome, idade)
            self.pode_voar = pode_voar

        def emitir_som(self):
            print(f"{self.nome} PIAA!.")

        def mover(self):
            if self.pode_voar:
                print(f"{self.nome} Voa no ceu.")
            else:
                print(f"{self.nome} Corre no chao.")

        def exibir_info(self):
            super().exibir_info()
            print(f"Pode voar: {'SIM' if self.pode_voar else 'NÂO'}")


#USO
c = Cachorro("Pirulito", 3, "Labrador")
p = Passaro("Loro", 6, True)
p2 = Passaro("Pinguim", 5, False)

c.exibir_info()
c.emitir_som()
c.mover()       

p.exibir_info()
p.emitir_som()      
p.mover()