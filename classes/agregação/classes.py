class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        tot = 0
        for produto in self.produtos:
            tot += produto.valor
        return tot

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
