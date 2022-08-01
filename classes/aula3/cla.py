from datetime import datetime
from random import randint

class Pessoa:
    atual = datetime.today().year
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        nasc = self.atual - self.idade
        return nasc

    @classmethod
    def por_ano_nascimento(cls, nome, nasc):
        idade = cls.atual - nasc
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand