#CLASSE PAI
class Trasporte:
    def __init__(self, nome):
        self.nome = nome

    def Viajar(self):
        print(f"Viajando de {self.nome}")

#CLASSE FILHA
class Aviao(Trasporte):
    def __init__(self, nome, velocidade):
        super().__init__(nome)
        self.velocidade = velocidade

    def Viajar(self):
        print(f"Viajando de {self.nome} a {self.velocidade} km/h")

#CLASSE FILHA
class Navio(Trasporte):
    def __init__(self, nome, tipo):
        super().__init__(nome)
        self.tipo = tipo

    def Viajar(self):
        print(f"Viajando de {self.nome} do tipo {self.tipo}")

#CLASSE FILHA
class trem(Trasporte):
    def __init__(self, nome, linhas):
        super().__init__(nome)
        self.linhas = linhas

    def Viajar(self):
        print(f"Viajando de {self.nome} com {self.linhas} linhas")


#USO
def iniciar_viagem(trasporte):
    trasporte.Viajar()

trasportes = [Aviao("Avião", 800), Navio("Navio", "Cruzeiro"), trem("Trem", 5)]
for Trasporte in trasportes:
    Trasporte.Viajar()









