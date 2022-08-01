class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Funcionario(Pessoa):
    def definir_salario(self, sal):
        self.salario = sal
    
    def aumento(self, taxaa):
        self.salario += self.salario * taxaa / 100
        return f'\033[1;32mNovo salário: R${self.salario:.2f}'
    def diminui(self, taxar):
        self.salario -= self.salario * taxar / 100
        return f'\033[1;32mNovo salário: R${self.salario:.2f}'

    def promocao(self):
        print('''Escolha um cargo:
[ 1 ] - Diretor de TI
[ 2 ] - Diretor de Marketing
[ 3 ] - Diretor de Operações
[ 4 ] - Diretor Financeiro
[ 5 ] - Diretor Executivo (CEO)
 ''')
 
