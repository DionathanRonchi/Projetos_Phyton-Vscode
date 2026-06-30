class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def apresentar(self):
        print(f"Olá! Meu nome é {self.nome}, tenho {self.idade} anos e moro em {self.cidade}.")


pessoas = []

while True:
    print("\n1- Cadastrar pessoa")
    print("2- Apresentar uma pessoa")
    print("3- Apresentar todas as pessoas")
    print("4- Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        nome = input("Nome: ")

        while True:
            idade_texto = input("Idade: ")
            if idade_texto.isdigit():
                idade = int(idade_texto)
                break
            print("Idade inválida, digite um número")

        cidade = input("Cidade: ")

        pessoas.append(Pessoa(nome, idade, cidade))
        print("Pessoa cadastrada com sucesso")

    elif opcao == "2":
        if len(pessoas) == 0:
            print("Nenhuma pessoa cadastrada")
        else:
            nome = input("Nome da pessoa: ")
            encontrou = False
            for pessoa in pessoas:
                if pessoa.nome == nome:
                    pessoa.apresentar()
                    encontrou = True
                    break
            if not encontrou:
                print("Pessoa não encontrada")

    elif opcao == "3":
        if len(pessoas) == 0:
            print("Nenhuma pessoa cadastrada")
        else:
            for pessoa in pessoas:
                pessoa.apresentar()

    elif opcao == "4":
        break

    else:
        print("Opção inválida")