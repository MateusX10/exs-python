from funcs import *


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos=1):
        if self.idade < 21:
            cont = self.idade
            tot = self.idade + anos
            while cont < tot:
                self.altura += 0.05
                cont += 1
                if cont == 21:
                    break
            print(f'Sua altura foi para {self.altura} m')
        print(f'{self.nome} que antes tinha {self.idade} anos agora passa a ter {self.idade + anos} anos')
        self.idade += anos

    def crescer(self, cm=1):
        cm = cm / 100
        cm = tirar_casas(cm)
        print(f'{self.nome} que antes media {self.altura} m, agora passar a media {self.altura+cm}')
        self.altura += cm

    def engordar(self, k=1):
        self.peso += k
        return self.peso

    def emagrecer(self, k=1):
        self.peso -= k
        return self.peso
