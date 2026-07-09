class Termostato:
    def __init__(self, temperatura=20):
        self.__temperatura = temperatura
        self.set_temperatura(temperatura)

    # GETTER
    def get_temperatura(self):
        return self.__temperatura

    # SETTER
    def set_temperatura(self, valor):
        if 16 <= valor <= 30:
            self.__temperatura = valor
        else:
            print("Temperatura inválida. Insira um valor entre 16 e 30 graus.")

    def exibir_status(self):
        print("=" * 30)
        print(f"Temperatura atual: {self.__temperatura}°C")
        print("=" * 30)


if __name__ == "__main__":
    t1 = Termostato()
    t1.set_temperatura(25)
    t1.set_temperatura(35)
    t1.set_temperatura(10)
    t1.exibir_status()