class Pessoa:
    falando = False
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        if self.falando:
            print(f'{self.nomeclasse} já está falando...')
            return
        print(f'{self.nomeclasse} está falando')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nomeclasse} não está falando...')
            return
        print(f'{self.nomeclasse} parou de falar')
        self.falando = False


class Cliente(Pessoa):
    def comprar(self, produto="computador"):
        print(f'{self.nomeclasse} comprou {produto}')


class Aluno(Pessoa):
    def estudar(self, materia="programação"):
        print(f'{self.nomeclasse} está estudando {materia}')