#CLASSE PAI
class funcionario:
    def __init__(self, nome, salario_Base):
        self.nome = nome
        self.salario_Base = salario_Base

    def calcularSalario(self):
        return self.salario_Base

    def exibirInfo(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R$ {self.calcularSalario():.2f}")
        print("-"*20)


#CLASSE FILHA
class Vendedor(funcionario):
    def __init__(self, nome, salario_Base, comissao):
        super().__init__(nome, salario_Base)
        self.comissao = comissao

    def calcularSalario(self):
        return self.salario_Base + self.comissao
    

class Gerente(funcionario):
    def __init__(self, nome, salario_Base, bonus):
        super().__init__(nome, salario_Base)
        self.bonus = bonus

    def calcularSalario(self):
        return self.salario_Base + self.bonus


#USO
f=funcionario("João", 2000)
v=Vendedor("Maria", 1800, 500)
g=Gerente("Carlos", 3000, 1000)

f.exibirInfo()
v.exibirInfo()
g.exibirInfo()
