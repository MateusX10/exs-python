from random import randint


class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def MudarValorLado(self):
        novo = randint(1, 99)
        print(f'O lado que antes valia {self.tamanho_lado} cm agora passa a valer {novo} cm')
        self.tamanho_lado = novo

    def MostrarValorLado(self):
        print(f'Valor do lado: {self.tamanho_lado} cm')

    def Area(self):
        a = self.tamanho_lado ** 2
        return f'A área vale {a} cm²'
