class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def inserir_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(f'Endereço: {endereco.cidade}, {endereco.estado}')

    def __del__(self):
        print(f'\033[1;31m{self.nome} FOI APAGADO\033[1;32m')



class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'\033[1;31m{self.cidade}/{self.estado} FOI APAGADO\033[m')