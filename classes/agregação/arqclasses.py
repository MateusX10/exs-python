class Casa:
    def __init__(self, comp, larg):
        self.comp = comp
        self.larg = larg
        self.chao = []

    def insere_chao(self, chao):
        self.chao.append(chao)

    def lista_chao(self):
        for chao in self.chao:
            print(chao.comprimento, chao.largura)

class Chao:
    def __init__(self, comp, larg):
        self.comprimento = comp
        self.largura = larg
    