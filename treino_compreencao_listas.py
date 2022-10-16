#Dobrar valores da lista

produtos = [500,1500,2000,500,100]

produtos2 = [preco * 2 for preco in produtos]

print(produtos)

print(produtos2)


'''novos_produtos = list()

for produto in produtos:
  novos_produtos.append(produto * 2)

print(f'Velhos produtos: {produtos}\nNovos produtos: {novos_produtos}')'''


# Produtos que custam mais de R$1000,00 recebem acréscimo de 50% sobre o valor total

ProdutosAcimaDeMil = []

for preco in produtos:
    if preco > 1000:
      ProdutosAcimaDeMil.append(preco + preco * 0.5)

print(ProdutosAcimaDeMil)

ProdutosAcimaDeMil = [(preco + (preco * 50 / 100)) for preco in produtos if preco > 1000]
print(ProdutosAcimaDeMil)
