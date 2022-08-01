from random import choice
class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def MostrarCor(self):
        print(f'Cor: {self.cor}')

    def TrocarCor(self):
        cores = ["vermelho", "azul", "verde", "amarelo", "branco", "preto", "cinza"]
        escolha = choice(cores)
        print(f'A cor "{self.cor}" foi trocada por {escolha}')
        self.cor = escolha
        

    