#CLASSE PAI
class funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcularSalario(self):
        return self.salario_base
    
    def exibirInfo(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: {self.calcularSalario()}")
        print("-" * 20)


#CLASSE FILHA
class horista(funcionario):
    def __init__(self, nome, salario_base, horas_trabalhadas, valor_hora):
        super().__init__(nome, salario_base)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcularSalario(self):
        return self.horas_trabalhadas * self.valor_hora

#CLASSE FILHA
class mensalista(funcionario):
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)

#USO
f = funcionario("João", 2000)
h = horista("Maria", 0, 40, 25)
m = mensalista("Carlos", 3000)

print("Funcionário:")
f.exibirInfo()

print("\nHorista:")
h.exibirInfo()

print("\nMensalista:")
m.exibirInfo()
