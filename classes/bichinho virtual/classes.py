from numeros import *
from mensagens import *
from time import sleep

class Bichinho:
    felicidade = 0
    def __init__(self, nome, idade, saude, fome):
        self.nome = nome
        self.idade = idade
        self.saude = saude
        self.fome = fome
        self.humor = self.horas = self.minutos = self.ComidaRecebida = self.brincar = None
        

    def show(self):
        print(f'''Nome: {self.nome}
Idade: {self.idade} anos
Fome: {self.fome}%
Saúde: {self.saude}%
Humor: {self.humor}
Tempo de brincadeira: {self.horas} horas e {self.minutos} minutos
Quantidade de comida: {self.ComidaRecebida} refeições p/ dia
''')

    @property
    def horas(self):
        return self._horas
    
    @horas.setter
    def horas(self, tempo):
        resp = ""
        while True:
            quant_horas = leiaInt('\033[1mInforme quantas horas p/dia você brinca com seu bichinho: ')
            while True:
                try:
                    resp = input(f'\033[1mVocê brinca com seu bichinho {quant_horas}H. p/dia, correto? [S/N]').strip().upper()[0]
                except:
                    SimOuNao() # Mensagem de erro
                    continue
                else:
                    if resp in "SN":
                        break
                    SimOuNao() # Mensagem de erro
               
            if resp == "S":
                break
            RetomandoPerguntas() #Dados incorretos, logo retoma-se perguntas
        self._horas = quant_horas

    @property  # Obtém os minutos
    def minutos(self):
        return self._minutos

    @minutos.setter # Configura os minutos
    def minutos(self, quant_minutos):
        while True:
            quant_minutos = leiaInt('\033[1mInforme agora o tempo em minutos que você brinca com seu bichinho: ')
            while True:
                try:
                    resp = str(input(f'\033[1mVocê brinca com seu bichinho {quant_minutos} min por dia, correto? [S/N] ')).strip().upper()[0]
                except:
                    SimOuNao() # Mensagem de erro

                else:
                    if resp in "SN":
                        break

            if resp == "N":
                RetomandoPerguntas() # Dados incorretos, logo retomam-se as perguntas
                continue

            break
        self._minutos = quant_minutos

    @property  # Obtém o valor
    def ComidaRecebida(self):
        return self._ComidaRecebida

    @ComidaRecebida.setter
    def ComidaRecebida(self, quant_comida): # Configura quantidade de comida recebida
        while True:
            quant_comida = leiaInt(f'\033[1mInforme quantas refeições você dá ao seu bichinho p/ dia: ')
            while True:
                try:
                    resp = str(input(f'\033[1mVocê oferece {quant_comida} refeições por dia ao seu bichinho, correto? [S/N]')).strip().upper()[0]

                except:
                    SimOuNao() # Mensagem de erro 

                else:
                    if resp in "SN":
                        break
                SimOuNao() # Mensagem de erro 
            if resp == "N":
                RetomandoPerguntas()
                continue
            break
        self._ComidaRecebida = quant_comida

    
    @property
    def brincar(self):
        return self._brincar

    @brincar.setter
    def brincar(self, valor):
        self.felicidade = 40
        print(f'{self.nome} está se divertindo muito...')
        for simbolo in range(0, 25):
            print('-=-', end='', flush=True)
            sleep(0.8)
        print()
        self._brincar = valor




    @property  #Obtém o valor
    def humor(self):
        return self._humor

    @humor.setter
    def humor(self, estado):  # Configura o humor
        self.felicidade += (self.saude + self.fome) / 2
        if 101 > self.felicidade >= 85:
            if 100 <= self.felicidade < 101:
                estado = "\033[1;34m (tão elegre que poderia morrer agora)\033[m"
            else:
                estado = "\033[1;32m (Muito feliz)\033[m"
        elif 85 >= self.felicidade >= 70:
            estado = "\033[1;32m (feliz)\033[m"

        elif 50 <= self.felicidade <= 70:
            estado = "\033[1;33m (mais ou menos)\033[m"

        elif self.felicidade < 50:
            if self.felicidade <= 0:
                estado =  f'\033[1;31m ({self.nome} morreu de tristeza)\033[m'
            else:
                estado = "\033[1;31m (triste)\033[m"

        else:
            estado = f' ({self.nome} morreu de alegria)'

        self._humor = str(f'{self.felicidade:.0f}') + "%" + estado

    


