from dado import *



preco = 0


preco = str(input("Preço: R$ ")).replace(",", ".")
preco = float(preco)

print(f"Aumentando 10% de {moedas(preco)}, temos {Aumentar(preco)}")
print(f"Diminuindo 30% de {moedas(preco)}, temos {Diminuir(preco, 30)}")
print(f"O dobro de {moedas(preco)} vale {Dobro(preco)}")
print(f"A metade de {moedas(preco)} vale {Metade(preco)}")

resumo(preco, 10, 13)

'''help(Aumentar)
help(Diminuir)
help(Dobro)
hel p(Metade)
help(moedas)'''

help(resumo)