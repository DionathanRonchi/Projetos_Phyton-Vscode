#CLASSE PAI 
class lampada:
    def __init__(self, marca): 
        self.marca = marca

    def acender(self):
        return f"A lâmpada {self.marca} está acendendo..."


#CLASSE FILHA
class LampadaIncandescente(lampada):
    def __init__(self, marca):
        super().__init__(marca)

    def acender(self):
        return f"{self.marca}: Luz quente e amarelada acesa."

#CLASSE FILHA
class LampadaFluorescente(lampada):
    def __init__(self, marca):
        super().__init__(marca)

    def acender(self):
        return f"{self.marca}: Luz branca fria acesa."

#CLASSE FILHA
class LampadaLED(lampada):
    def __init__(self, marca):
        super().__init__(marca)

    def acender(self):
        return f"{self.marca}: Luz LED de baixo consumo acesa."

#USO
lampadas = [LampadaIncandescente("Philips"), LampadaFluorescente("Osram"), LampadaLED("GE")]
for lampada in lampadas:
    print(lampada.acender())





