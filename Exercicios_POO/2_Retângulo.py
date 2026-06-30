class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

    def exibir_info(self):
        area = self.calcular_area()
        perimetro = self.calcular_perimetro()
        print(f"Retângulo {self.largura}x{self.altura} -> "
              f"Área: {area} | Perímetro: {perimetro}")


def ler_numero(mensagem):
    while True:
        texto = input(mensagem)
        try:
            return float(texto)
        except ValueError:
            print("Valor inválido, digite um número")


retangulos = []

while True:
    print("\n1- Cadastrar retângulo")
    print("2- Exibir informações de um retângulo")
    print("3- Listar todos os retângulos")
    print("4- Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        largura = ler_numero("Largura: ")
        altura = ler_numero("Altura: ")
        retangulos.append(Retangulo(largura, altura))
        print("Retângulo cadastrado com sucesso")

    elif opcao == "2":
        if len(retangulos) == 0:
            print("Nenhum retângulo cadastrado")
        else:
            print("\nRetângulos Cadastrados")
            contador = 1
            for retangulo in retangulos:
                print(f"{contador} - {retangulo.largura} x {retangulo.altura}")
                contador += 1

            indice = input("Digite o número do retângulo para ver os detalhes: ")
            if indice.isdigit() and 1 <= int(indice) <= len(retangulos):
                retangulos[int(indice) - 1].exibir_info()
            else:
                print("Retângulo não encontrado")

    elif opcao == "3":
        if len(retangulos) == 0:
            print("Nenhum retângulo cadastrado")
        else:
            for retangulo in retangulos:
                retangulo.exibir_info()

    elif opcao == "4":
        break

    else:
        print("Opção inválida")