class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.endereco = []

    def insere_endereco(self, cidade, estado):
        self.endereco.append(Endereco(cidade, estado))

    def lista_endereco(self):
        for endereco in self.endereco:
            print(endereco.cidade, endereco.estado)
            endereco.enderecar()

    def __del__(self):
        print('\033[1;31mCliente apagado\033[m')
   


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def enderecar(self):
        print('Iniciando processo de endereçamento...')

    def __del__(self):
        print('\033[1;31mEndereço apagado\033[m')
