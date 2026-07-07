class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.__nota = nota
        self.set_nota(nota)
    
    #GETTER
    def get_nota(self):
        return self.__nota

    #SETTER
    def set_nota(self, nova_nota):
        if 0 <= nova_nota <= 10:
            self.__nota = nova_nota
        else:
            print("Nota inválida. Por favor, insira um valor entre 0 e 10.")
    
    def situacao(self):
        if self.__nota >= 6:
            return "Aprovado"
        elif self.__nota >= 4:
            return "Recuperação"
        else:
            return "Reprovado"

    def exibir_info(self):
        print(f"Aluno: {self.nome}")
        print(f"Nota: {self.__nota}")
        print(f"Situação: {self.situacao()}")
        print("=" * 30)


if __name__ == "__main__":
    a1 = Aluno(nome="Dionathan", nota=7.5)
    a1.exibir_info()

    a2 = Aluno(nome="Jhon", nota=2)
    a2.exibir_info()










