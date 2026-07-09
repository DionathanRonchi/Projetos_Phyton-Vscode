agenda = {}

while True:
    print("\n1- Cadastrar")
    print("2- Consultar")
    print("3- Listar Contatos")
    print("4- Sair")
    
    print("6-Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        if nome in agenda:
            print("Nome ja cadastrado")
        else:
            while True:
                telefone = input("Telefone: ")
                if telefone != "":
                    break
                print("Telefone obrigatorio")

            agenda[nome] = telefone
            print("Contato cadastrado")
    elif opcao == "2":
        nome = input("Nome para buscar: ")
        if nome in agenda:
            print("Telefone", agenda[nome])
        else:
            print("Contato não encontrado")
    elif opcao == "3":
        if len(agenda) == 0:
            print("Agenda Vazia")
        else:
            print("\nContatos Cadastrados")
            contador = 1
            #for que percorre dois argumentos
            for nome, telefone in agenda.items():
                print(f"{contador} - {nome} - {telefone}")
                contador += 1

    elif opcao == "4":
        letra = input("Digite uma letra Inicial: ").upper()
        encontrou = False

    for nome, telefone in agenda.items():
        if nome.upper().startswith(letra):
            print(f"{nome} - {telefone}")
            encontrou = True

    if not encontrou:
        print("Agenda Vazia")

    elif opcao == "5":
        nome = input("Nome para excluir: ")
        if nome in agenda:
            del agenda[nome]
            print("Cpntado removido")
        else:
            print("Contato não enconrado")


    elif opcao == "6":
        break