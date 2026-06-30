class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade += valor

    def frear(self, valor):
        self.velocidade -= valor
        if self.velocidade < 0:
            self.velocidade = 0

    def exibir_status(self):
        print(f"Carro: {self.marca} {self.modelo} ({self.ano}) | "
              f"Velocidade atual: {self.velocidade} km/h")


def ler_numero(mensagem):
    while True:
        texto = input(mensagem)
        if texto.isdigit():
            return int(texto)
        print("Valor inválido, digite um número")


def escolher_carro(carros):
    if len(carros) == 0:
        print("Nenhum carro cadastrado")
        return None

    print("\nCarros Cadastrados")
    contador = 1
    for carro in carros:
        print(f"{contador} - {carro.marca} {carro.modelo} ({carro.ano})")
        contador += 1

    indice = input("Digite o número do carro: ")
    if indice.isdigit() and 1 <= int(indice) <= len(carros):
        return carros[int(indice) - 1]

    print("Carro não encontrado")
    return None


carros = []

while True:
    print("\n1- Cadastrar carro")
    print("2- Acelerar")
    print("3- Frear")
    print("4- Exibir status de um carro")
    print("5- Listar todos os carros")
    print("6- Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        ano = ler_numero("Ano: ")
        carros.append(Carro(marca, modelo, ano))
        print("Carro cadastrado com sucesso")

    elif opcao == "2":
        carro = escolher_carro(carros)
        if carro is not None:
            valor = ler_numero("Valor para acelerar: ")
            carro.acelerar(valor)
            carro.exibir_status()

    elif opcao == "3":
        carro = escolher_carro(carros)
        if carro is not None:
            valor = ler_numero("Valor para frear: ")
            carro.frear(valor)
            carro.exibir_status()

    elif opcao == "4":
        carro = escolher_carro(carros)
        if carro is not None:
            carro.exibir_status()

    elif opcao == "5":
        if len(carros) == 0:
            print("Nenhum carro cadastrado")
        else:
            for carro in carros:
                carro.exibir_status()

    elif opcao == "6":
        break

    else:
        print("Opção inválida")