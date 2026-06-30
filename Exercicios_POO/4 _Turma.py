class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def matricular(self, nome_aluno):
        if nome_aluno in self.alunos:
            print(f"O aluno '{nome_aluno}' já está matriculado na turma {self.nome}.")
        else:
            self.alunos.append(nome_aluno)
            print(f"Aluno '{nome_aluno}' matriculado com sucesso na turma {self.nome}.")

    def remover(self, nome_aluno):
        if nome_aluno in self.alunos:
            self.alunos.remove(nome_aluno)
            print(f"Aluno '{nome_aluno}' removido da turma {self.nome}.")
        else:
            print(f"Aluno '{nome_aluno}' não encontrado na turma {self.nome}.")

    def listar_alunos(self):
        if len(self.alunos) == 0:
            print(f"A turma {self.nome} não possui alunos matriculados")
        else:
            print(f"\nAlunos da turma {self.nome} (ordem alfabética)")
            contador = 1
            for aluno in sorted(self.alunos):
                print(f"{contador} - {aluno}")
                contador += 1
            print(f"Total de alunos: {len(self.alunos)}")

    def esta_matriculado(self, nome_aluno):
        matriculado = nome_aluno in self.alunos
        if matriculado:
            print(f"'{nome_aluno}' está matriculado na turma {self.nome}.")
        else:
            print(f"'{nome_aluno}' NÃO está matriculado na turma {self.nome}.")
        return matriculado


nome_turma = input("Nome da turma: ")
turma = Turma(nome_turma)

while True:
    print("\n1- Matricular aluno")
    print("2- Remover aluno")
    print("3- Listar alunos")
    print("4- Verificar se um aluno está matriculado")
    print("5- Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        nome_aluno = input("Nome do aluno: ")
        turma.matricular(nome_aluno)

    elif opcao == "2":
        nome_aluno = input("Nome do aluno para remover: ")
        turma.remover(nome_aluno)

    elif opcao == "3":
        turma.listar_alunos()

    elif opcao == "4":
        nome_aluno = input("Nome do aluno: ")
        turma.esta_matriculado(nome_aluno)

    elif opcao == "5":
        break

    else:
        print("Opção inválida")