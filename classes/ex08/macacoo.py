from time import sleep

class Macaco:
    def __init__(self, nome,bucho, comendo=False):
        self.nome = nome
        self.bucho = bucho
        self.comendo = comendo

    def show(self):
        print(f'Nome: {self.nome}\nBucho: {self.bucho}')

    def comer(self, comida='banana'):
        if self.bucho == "cheio":
            print(f'{self.nome} está com o bucho cheio')
            return
        print(f'{self.nome} está comendo {comida}')
        self.bucho = "cheio"
        self.comendo = True

    def PararComer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False

    def digerir(self, comida="banana"):
        if not self.comendo:
            print(f'{self.nome} não tem o que digerir')
            return
        print(f'{self.nome} está digirindo {comida}...')
        sleep(1.5)
        print(f'{self.nome} está pronto para encher mais o bucho!')
        self.comendo = False

    def VerBucho(self):
        print(f'Bucho de {self.nome}: {self.bucho}')

    def canibalismo(self, parceiro):
        print(f'{self.nome} começou a comer {parceiro.nome}')
        print(f'{parceiro.nome} já não existe mais neste mundo...')