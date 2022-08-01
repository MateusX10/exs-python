class Bichinho:
    def __init__(self, nome, idade, saude, fome=False, humor=False):
        self.nome = nome
        self.idade = idade
        self.saude = saude
        self.fome = fome
        self.humor = humor

    def show(self):
        print(f'''Nome: {self.nome} \nIdade: {self.idade} anos
Saúde: {self.saude}\ncom fome? {self.fome}\nHumor: {self.humor}''')

    def AlterarNome(self):
        novo = str(input('Novo nome: '))
        self.nome = novo
        print(f'\033[1;32mNome redefinido para "{self.nome}" com sucesso\033[m')
    
    def AlterarIdade(self):
        while True:
            novo = int(input('Nova idade: '))
            if novo > 0:
                break
            print('\033[1;31mIdade inválida\033[m')
        self.idade = novo
        print(f'\033[1;32mIdade redefinida para {self.idade} anos com sucesso\033[m')
    
    def AlterarSaude(self):
        while True:
            opcs = ["boa", "mediana", "ruim"]
            print('''Suas opções:
    [ 1 ] - boa
    [ 2 ] - mediana
    [ 3 ] - Ruim
''')
            novo = int(input('Novo estado de saúde: '))
            try:
                self.saude = opcs[novo-1]
            except:
                print('\033[1;31mERRO!Escolha uma opção válida!\033[m')
                continue
            else:
                print(f'\033[1;32mNovo estado de saúde redefinido como "{self.saude}" com sucesso\033[m')
            break

    def AlterarFome(self):
        novo = 0
        while True:
            print('''Suas opções:
    [ 1 ] - Com fome
    [ 2 ] - Sem fome''')
            novo = int(input('Qual a sua escolha? '))
            if 0 < novo <= 2:
                print(f'\033[1;32mFome alterada com sucesso\033[m')
                break
            print('\033[1;31mTente novamente\033[m')
        if novo == 1:
            self.fome = True
        else:
            self.fome = False
    
    def ConfigHumor(self):
        if self.saude == "boa" or self.saude == "mediana" and not self.fome:
            self.humor = True
        else:
            self.humor = False