from classes import *

carrinho = CarrinhoDeCompras()
p1 = Produto("pão", 10)
p2 = Produto("lanche", 5)
p3 = Produto("brinquedo", 20)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.listar_produtos()
print(carrinho.soma_total())