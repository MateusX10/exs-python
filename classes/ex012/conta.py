class ContaInvestimento:
    def __init__(self, valor, taxaJuros):
        self.valor = valor
        self.taxaJuros = taxaJuros

    def StatusConta(self):
        tot = self.valor + (self.valor * self.taxaJuros / 100)
        print(f'''Valor a pagar: R${self.valor:.2f}
Taxa de juros: {self.taxaJuros}
Total a pagar: R${tot:.2f}''')

    def AdcionarJuros(self):
        self.valor += self.valor * 10 / 100
        print(f'Novo valor a pagar: R${self.valor}')