from agregacao import Produto, CarrinhoCompra

carrinho1 = CarrinhoCompra()

p1 = Produto("porta", 200)
p2 = Produto("calça", 45)
p3 = Produto("macbook", 12000)

carrinho1.inserir_produtos(p1)
carrinho1.inserir_produtos(p2)
carrinho1.inserir_produtos(p3)
carrinho1.inserir_produtos(p3)
carrinho1.inserir_produtos(p1)
carrinho1.inserir_produtos(p2)
carrinho1.listar_produtos()
print(carrinho1.soma_total())