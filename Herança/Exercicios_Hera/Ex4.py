#CLASSE PAI
class forma:
    def __init__(self, cor):
        self.cor = cor

    def calcularArea(self):
        pass

    def exibirInfo(self):
        print(f"Área: {self.calcularArea()}")
        print(f"Cor: {self.cor}")
        print("-" * 20)


#CLASSE FILHA
class circulo(forma):
    def __init__(self, cor, raio):
        super().__init__(cor)
        self.raio = raio

    def calcularArea(self):
        return 3.14 * self.raio ** 2

#CLASSE FILHA
class retangulo(forma):
    def __init__(self, cor, largura, altura):
        super().__init__(cor)
        self.largura = largura
        self.altura = altura

    def calcularArea(self):
        return self.largura * self.altura

#CLASSE FILHA
class triangulo(forma):
    def __init__(self, cor, base, altura):
        super().__init__(cor)
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return (self.base * self.altura) / 2
    
#USO
c = circulo("Vermelho", 5)
r = retangulo("Azul", 4, 6)
t = triangulo("Verde", 10, 2)

c.exibirInfo()
r.exibirInfo()  
t.exibirInfo()