#CLASSE PAI
class animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print(f"O {self.nome} emite um som.")

#CLASSE FILHA
class cachorro(animal):
    def emitir_som(self):
        print(f"O {self.nome} late.")

#CLASSE FILHA
class gato(animal):
    def emitir_som(self):
        print(f"O {self.nome} mia.")

#USO
def fazer_barulho(animal):
    animal.emitir_som() 

animais = [cachorro("Scooby"), gato("Tom"), cachorro("Coragem"), gato("Garfield")]
for animal in animais:
    fazer_barulho(animal)
