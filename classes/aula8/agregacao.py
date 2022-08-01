class CarrinhoCompra:
    def __init__(self):
        self.produtos = []

    def inserir_produtos(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(f'Nome: {produto.nome}, Preço: R${produto.valor}')

    def soma_total(self):
        tot = 0
        for produto in self.produtos:
            tot += produto.valor
        return f'Total: R${tot:.2f}'

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor