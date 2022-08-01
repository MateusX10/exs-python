from numeros import *

class BombaCombustivel:
    def __init__(self, tipoCombustivel, ValorLitro, Quant_Comb):
        self.tipoCombustivel = tipoCombustivel
        self.ValorLitro = ValorLitro
        self.Quant_comb = Quant_Comb
    
    def ViewInfo(self):
        print(f'''Tipo do combustível: {self.tipoCombustivel}
Valor do litro: R${self.ValorLitro:.2f}
Quantidade de combustível: {self.Quant_comb}''')

    def AbastecerValor(self):
        tipo = valor = novo = preco_litro = 0
        preco_litro = self.ValorLitro
        valor = leiaInt("Quanto quer gastar? ")
        novo = valor / preco_litro
        print(f'Gastando R${valor:.2f}, você pode abastecer seu carro com R${novo:.1f} litros')

    def AbasterLitro(self):
        custo = valor_pagar = 0
        custo = self.ValorLitro
        litros = leiaFloat("Encher o carro com quantos litros? ")
        valor_pagar = custo * litros
        print(f'Com {litros:.1f} litros, você pagará no final R${valor_pagar:.2f}')

    def AlterarLitro(self):
        quant = leiaFloat('Alterar o valor do litro para quanto? ')
        self.ValorLitro = quant
        print(f'Novo valor do litro: R${self.ValorLitro:.2f}')

    def AlterarComb(self):
        print('''Opções:
[ 1 ] - Gasolina
[ 2 ] - Diesel
[ 3 ] - Etanol
''')    
        while True:
            escolha = leiaInt("Mudar para qual? ")
            if 0 < escolha < 4:
                if escolha == 1:
                    self.tipoCombustivel = "gasolina"
                elif escolha == 2:
                    self.tipoCombustivel = "diesel"
                else:
                    self.tipoCombustivel = "etanol"
                break
            print('\033[1;31mERRO!Digite uma opção válida!\033[m')

    def AlterarQuant(self):
        escolha = leiaFloat('Alterar para quanto? ')
        self.Quant_Comb = escolha
        print(f'\033[1;32mQuantidade de combustível alterada para {self.Quant_Comb}L com sucesso\033[m')
    