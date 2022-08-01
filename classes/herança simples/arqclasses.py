class Dispositivo:
    from time import sleep
    ligado = False
    def __init__(self, marca, tamanho_tela, cpu, disco, ram):
        self.marca = marca
        self.tamanho_tela = tamanho_tela
        self.cpu = cpu
        self.disco = disco
        self.ram = ram
        self.nomeclasse = self.__class__.__name__

    def teclar(self, tecla="space"):
        print(f'{self.nomeclasse} está teclando a tecla {tecla}')

    def ligar(self):
        if self.ligado:
            print(f'{self.nomeclasse} já está ligado...')
            return
        print(f'{self.nomeclasse} está ligando...')
        self.sleep(1.5)
        print('\033[1;32mPronto!\033[m')
        self.ligado = True

    def desligar(self):
        if not self.ligado:
            print(f'{self.nomeclasse} já está desligado...')
            return
        print(f'{self.nomeclasse} está desligando...')
        self.sleep(1.5)
        print("\033[1;32mPronto!\033[m")
        self.ligado = False

class Computador(Dispositivo):
    def mousear(self, canto_tela="menu"):
        print(f'Computador está clicando no {canto_tela} da tela')

class Celular(Dispositivo):
    def tirar_foto(self):
        print(f'Celular está tirando foto...')

class Tv(Dispositivo):
    def mudar_canal(self, canal="7"):
        print(f'TV está mudando de canal para {canal}')

class Tablet(Dispositivo):
    def imitar(self):
        print('Tablet está fazendo o possível para imitar o celular...')
        


