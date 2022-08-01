from getset import Produto

prod1 = Produto("Camiseta", "R$30")
prod2 = Produto("Mochila", 40)

prod1.desconto(10)
print(prod1.nome, prod1.preco)
print(prod2.nome, prod2.preco)