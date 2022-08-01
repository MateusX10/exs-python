class Funcionario:
    def __init__(self, nome):
        self.__nome = nome
        self.__salario = []
        self.algo = None

    @property
    def nome(self):
        return self.__nome

    @property
    def salario(self):
        return self.__salario

    def adcionar_salario(self, valor1, valor2):
        self.salario.append(Salar(valor1, valor2))

    def ExibirSalario(self):
        for salario in self.salario:
            return f'''Salário1: R${salario.valor1:.2f}
Salário2: R${salario.valor2:.2f}
Total: R${salario.valor1 + salario.valor2:.2f}'''

    def __del__(self):
        print(f'\033[1;31m{self.nome} FOI APAGADO\033[m')

class Salar:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def __del__(self):
        print(f'\033[1;31m{self.valor1}/{self.valor2} FOI APAGADO\033[m')

class Chefe:
    def __init__(self, nome, humor):
        self.__nome = nome
        self.humor = humor

    @property
    def humor(self):
        return self._humor

    @humor.setter
    def humor(self, novo):
        novo = "feliz ao ponto de dar 200% de aumento"
        self._humor = novo


    def aumento(self):
        print(f'Você recebeu um aumento, mas isso não foi de fato efetivado :)')

    def desconto(self):
        print('Você recebeu um desconto, boa sorte com o dinheiro :)')

class Pagador:
    def __init__(self, quantidade):
        self.quantidade = quantidade

        


    
