from moeda import *

preco = float(input("Preço: R$ "))

print(f"Aumentando 10% de {moedas(preco)}, temos {moedas(Aumentar(preco))}")
print(f"Diminuindo 30% de {moedas(preco)}, temos {moedas(Diminuir(preco, 30))}")
print(f"O dobro de {moedas(preco)} vale {moedas(Dobro(preco))}")
print(f"A metade de {moedas(preco)} vale {moedas(Metade(preco))}")