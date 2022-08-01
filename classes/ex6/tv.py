class Tv:
    def __init__(self, canal,volume):
        self.canal = canal
        self.volume = volume

    def aumentar(self):
        quant = 0
        while True:
            quant = int(input('Aumentar o volume em quanto? '))
            novo = self.volume + quant
            if 0 <= novo <= 100:
                break
            print(f'\033[1;31mImpossível redefinir o volume para {novo}\033[m')
        self.volume += quant
        print(f'\033[1;32mVolume redefinido para {self.volume} com sucesso.\033[m')

    def diminuir(self):
        while True:
            quant = int(input('Diminuir o volume em quanto? '))
            novo = (self.volume - quant) 
            if novo >= 0:
                break
            print(f'\033[1;31mImpossível redefinir o volume para {novo}\033[m')
        self.volume -= quant
        print(f'\033[1;32mVolume redefinido para {self.volume} com sucesso.\033[m')

    def MudarCanal(self):
        novo = 0
        while True:
            novo = int(input('Mudar para qual canal? '))
            if 0 < novo <= 300:
                break
            print(f'\033[1;31m"{novo}" não é um canal válido.\033[m')
        self.canal = novo
        print(f'\033[1,32mCanal redefinido para {self.canal} com sucesso!\033[m')
