TotCompra = ProdutoMaior1000 = PrecoMaisBarato = cont = 0
NomeProdutoMaisBarato = ""


while True:
    cont += 1
    nome = str(input('Nome do produto: ')).strip().capitalize()
    preco = float(input("Preço: R$"))
    TotCompra += preco
    if preco > 1000:
        ProdutoMaior1000 += 1

    if cont == 1:
        PrecoMaisBarato = preco
        NomeProdutoMaisBarato = nome
    else:
        if preco < PrecoMaisBarato:
            PrecoMaisBarato = preco
            NomeProdutoMaisBarato = nome

    r = "q"
    while r not in "SsNn":
        r = str(input("Continuar [S/N]? ")).strip().upper()[0]

    if r == "N":
        break

print(f"O total da compra foi de R${TotCompra:.2f}")
print(f"Temos {ProdutoMaior1000} produtos custando mais de R$1000,00")
print(f"O produto mais barato foi {NomeProdutoMaisBarato} que custa R${PrecoMaisBarato:.2f}")