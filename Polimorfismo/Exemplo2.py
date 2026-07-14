#CLASSE PAI
class Forma:
    def __init__(self, nome = "Forma Genérica"):
        self.nome = nome

    def calcularArea(self):
        return 0

    def descricao(self):
        return self.nome

    def exibirArea(self):
        print(f"{self.descricao()} - Area: {self.calcularArea()}")

#CLASSE FILHA
class Circulo(Forma):
    def __init__(self, nome, raio):
        super().__init__("Círculo")
        self.raio = raio
    def calcularArea(self):
        return 3.1415 * self.raio ** 2
    
    def descricao(self):
        return f"{self.nome} (raio={self.raio})"
    
#CLASSE FILHA
class Retangulo(Forma):
    def __init__(self, nome, largura, altura):
        super().__init__("Retângulo")
        self.largura = largura
        self.altura = altura
    def calcularArea(self):
        return self.largura * self.altura
   
    def descricao(self):
        return f"{self.nome}({self.largura} * {self.altura})"

    def exibirArea(self):
        print(f"{self.descricao()} - Area: {self.calcularArea()}")

#USO   
formas = [Circulo("Círculo", 5), Retangulo("Retângulo", 4, 6), Circulo("Círculo", 10), Retangulo("Retângulo", 2, 4)]
for forma in formas:
    forma.exibirArea()