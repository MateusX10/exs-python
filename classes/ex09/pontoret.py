class Ponto:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def imprimir(self):
        print(f'''Valor de "X": {self.x}
Valor de "Y": {self.y}''')

class Retangulo:
    def __init__(self, larg, alt):
        self.larg = larg
        self.alt = alt

    def centro(self):
        res = self.larg / 2 + self.alt / 2
        return res

    def menu(self):
        while True:
            try:
                novo_larg = float(input('Novo valor da largura: '))
                novo_alt = float(input('Novo valor da altura: '))
            except:
                print('\033[1;31mOcorreu um erro.Tente novamente\033[m')
                continue
            else:
                self.larg = novo_larg
                self.alt = novo_alt
                break