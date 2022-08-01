from datetime import datetime


class Pessoa:
    ano_atual = datetime.today().year
    def __init__(self, nome, idade, falando=False, comendo=False):
        self.nome = nome
        self.idade = idade
        self.falando = falando
        self.comendo = comendo

    def comer(self, comida="batata frita"):
        if self.falando:
            print(f'{self.nome} não pode comer enquanto fala')
            return
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return
        print(f'{self.nome} está comendo {comida}...')
        self.comendo = True

    def PararComer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False

    def falar(self, assunto="POO"):
        if self.comendo:
            print(f'{self.nome} não pode falar enquanto come')
            return
        if self.falando:
            print(f'{self.nome} já está falando...')
            return
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def PararFalar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
        print(f'{self.nome} parou de falar')
        self.falando = False

    def get_ano_nascimento(self):
        ano_nascimento = self.ano_atual - self.idade
        return ano_nascimento

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)