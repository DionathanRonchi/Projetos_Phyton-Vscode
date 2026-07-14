#CLASSE PAI
class veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca  
        self.modelo = modelo
        self.ano = ano

    def exibirInfo(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print("-"*20)


#CLASSE FILHA
class Carro(veiculo):
    def __init__(self, marca, modelo, ano, numero_portas):
        super().__init__(marca, modelo, ano)
        self.portas = numero_portas

    def exibirInfo(self):
        super().exibirInfo()
        print(f"Portas: {self.portas}")
        print("-"*20)


#CLASSE FILHA
class Moto(veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

    def exibirInfo(self):
        super().exibirInfo()
        print(f"Cilindradas: {self.cilindradas}")
        print("-"*20)

#USO
c = Carro("Toyota", "Corolla", 2020, 4)
m = Moto("Honda", "CB500", 2019, 500)
c.exibirInfo()
m.exibirInfo()
