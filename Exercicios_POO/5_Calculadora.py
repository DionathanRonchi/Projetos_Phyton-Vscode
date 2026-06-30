class Calculadora:
    def __init__(self):
        self.historico = []

    def somar(self, a, b):
        resultado = a + b
        self.historico.append(f"{a} + {b} = {resultado}")
        return resultado

    def subtrair(self, a, b):
        resultado = a - b
        self.historico.append(f"{a} - {b} = {resultado}")
        return resultado

    def multiplicar(self, a, b):
        resultado = a * b
        self.historico.append(f"{a} * {b} = {resultado}")
        return resultado

    def dividir(self, a, b):
        if b == 0:
            print("Aviso: não é possível dividir por zero!")
            self.historico.append(f"{a} / {b} = ERRO (divisão por zero)")
            return None
        resultado = a / b
        self.historico.append(f"{a} / {b} = {resultado}")
        return resultado

    def exibir_historico(self):
        if not self.historico:
            print("O histórico está vazio.")
        else:
            print("\nHistórico de operações:")
            for operacao in self.historico:
                print(f" - {operacao}")


def ler_numero(mensagem):
    while True:
        texto = input(mensagem)
        try:
            return float(texto)
        except ValueError:
            print("Valor inválido, digite um número")


calc = Calculadora()

while True:
    print("\n1- Somar")
    print("2- Subtrair")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Exibir histórico")
    print("6- Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        a = ler_numero("Primeiro valor: ")
        b = ler_numero("Segundo valor: ")
        print("Resultado:", calc.somar(a, b))

    elif opcao == "2":
        a = ler_numero("Primeiro valor: ")
        b = ler_numero("Segundo valor: ")
        print("Resultado:", calc.subtrair(a, b))

    elif opcao == "3":
        a = ler_numero("Primeiro valor: ")
        b = ler_numero("Segundo valor: ")
        print("Resultado:", calc.multiplicar(a, b))

    elif opcao == "4":
        a = ler_numero("Primeiro valor: ")
        b = ler_numero("Segundo valor: ")
        resultado = calc.dividir(a, b)
        if resultado is not None:
            print("Resultado:", resultado)

    elif opcao == "5":
        calc.exibir_historico()

    elif opcao == "6":
        break

    else:
        print("Opção inválida")