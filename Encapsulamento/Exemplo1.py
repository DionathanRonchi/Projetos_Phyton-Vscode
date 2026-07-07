class Paciente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.__cpf = cpf
        self.__idade = idade
        self.__historico = []

    # GET
    def get_cpf(self):
        cpf = self.__cpf
        return f"***.***.{cpf[8:11]}---{cpf[11:]}"

    def get_idade(self):
        return self.__idade

    def get_historico(self):
        return list(self.__historico)

    # SETTER
    def set_idade(self, nova_idade):
        if nova_idade > 0:
            self.__idade = nova_idade
        else:
            print("Idade inválida")

    # MÉTODOS
    def adicionar_historico(self, diagnostico):
        self.__historico.append(diagnostico)
        print(f"Diagnostico registrado: {diagnostico}")

    def exibir_prontuario(self):
        print("=" * 30)
        print(f"Paciente: {self.nome}")
        print(f"CPF: {self.get_cpf()}")
        print(f"Idade: {self.get_idade()}")
        print("Histórico:")
        historico = self.get_historico()
        if historico:
            for diagnostico in historico:
                print(f" - {diagnostico}")
        else:
            print("Não há histórico registrado.")
        print("=" * 30)


if __name__ == "__main__":
    p1 = Paciente("João", "123456789012", 29)
    p1.set_idade(30)
    p1.exibir_prontuario()

    

