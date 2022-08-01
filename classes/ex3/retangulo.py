from random import randint


class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
    
    def MostrarLados(self):
        return f'Medida de {self.largura}X{self.comprimento} cm²'

    def MudarLados(self):
        novo_larg = randint(1, 99)
        novo_comp = randint(1,99)
        print(f'medida de {self.largura}X{self.comprimento} cm² alterado para {novo_larg}X{novo_comp} cm²')
        self.comprimento = novo_comp
        self.largura = novo_larg

    def area(self):
        a = self.comprimento * self.largura
        return a

    def perimetro(self):
        p = 2 * (self.comprimento + self.largura)
        return p

    def AjustarCasa(self):
        a = self.comprimento* self.largura
        valor_piso = 40
        valor_rodape = 10
        rodape_por_piso = valor_piso / valor_rodape
        pisos = a / valor_piso
        print(f'''Área do local: {a} m²
Valor do piso: {valor_piso} cm
Valor do rodapé: {valor_rodape} cm
Rodapé por piso: {rodape_por_piso}
Pisos necessários: {pisos}''')
        