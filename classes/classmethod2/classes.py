class Robo:
    def __init__(self, nome, id, cor, func):
        self.nome = nome
        self.id = id
        self.cor = cor
        self.func = func

    @classmethod
    def reset(cls, nome, id, cor):
        funcao = 0
        opcs = ["faxineiro", "lutador", "assassino", "suporte", "garçom"]
        print('''[ 1 ] - Faxineiro
[ 2 ] - Lutador
[ 3 ] - Assassino
[ 4 ] - Suporte
[ 5 ] - Garçom
''')
        while True:
            funcao = int(input('Escolha uma função para o robô: '))
            if funcao > 0 and funcao < 6:
                break
        print(f'Função definida para {opcs[funcao-1]} com sucesso')
        return cls(nome, id, cor, funcao)

    def ExibirRoboInfo(self):
        print(f'''Nome: {self.nome}
ID: {self.id}
Cor: {self.cor}
Função: {self.func}''')

