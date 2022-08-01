from datetime import datetime


class Pessoa:
    ano_atual = datetime.today().year
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        ano_nascimento = self.ano_atual - self.idade
        return ano_nascimento

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)