class Relogio:
    def __init__(self, h=0, m=0, s=0):
        self.__horas = 0
        self.__minutos = 0
        self.__segundos = 0
        self.set_hora(h, m, s)

    # GETTER
    def get_hora(self):
        return f"{self.__horas:02d}:{self.__minutos:02d}:{self.__segundos:02d}"

    # SETTER
    def set_hora(self, h, m, s):
        if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
            self.__horas = h
            self.__minutos = m
            self.__segundos = s
        else:
            print("Horário inválido. Horas: 0-23, minutos e segundos: 0-59.")

    # MÉTODOS
    def avancar_segundo(self):
        self.__segundos += 1
        if self.__segundos >= 60:
            self.__segundos = 0
            self.__minutos += 1
            if self.__minutos >= 60:
                self.__minutos = 0
                self.__horas += 1
                if self.__horas >= 24:
                    self.__horas = 0

    def exibir(self):
        print("=" * 30)
        print(f"Horário atual: {self.get_hora()}")
        print("=" * 30)


if __name__ == "__main__":
    r1 = Relogio(h=23, m=59, s=58)
    r1.exibir()

    for _ in range(5):
        r1.avancar_segundo()
        r1.exibir()

    r1.set_hora(25, 0, 0)
    print("Hora final:", r1.get_hora())