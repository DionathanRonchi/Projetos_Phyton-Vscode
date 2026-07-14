#CLASSE PAI
class Funcionario:
    def __init__(self, nome, cumprimentar):
        self.nome = nome
        self.cumprimentar = cumprimentar

    def cumprimentar_funcionario(self):
        return f"Olá, meu nome é {self.nome}."

#CLASSE FILHA
class Recepcionista(Funcionario):
    def __init__(self, nome, cumprimentar):
        super().__init__(nome, cumprimentar)

    def cumprimentar_funcionario(self):
        return f"Bem-vindo(a)!Meu nome é {self.nome}, posso ajudar?"

#CLASSE FILHA
class Gerente(Funcionario):
    def __init__(self, nome, cumprimentar):
        super().__init__(nome, cumprimentar)

    def cumprimentar_funcionario(self):
        return f"Olá, sou {self.nome}, gerente desta unidade."

#CLASSE FILHA
class Tecnico(Funcionario):
    def __init__(self, nome, cumprimentar):
        super().__init__(nome, cumprimentar)

    def cumprimentar_funcionario(self):
        return f"Oi, sou {self.nome}, do suporte técnico da empresa."


#USO
funcionarios = [Recepcionista("Ana", "Bem-vindo(a)!"), Gerente("Carlos", "Olá, sou o gerente."), Tecnico("Lucas", "Oi, sou do suporte técnico.")]
for funcionario in funcionarios:
    print(funcionario.cumprimentar_funcionario())
