from moeda2 import *

preco = float(input("Preço: R$ "))

print(f"Aumentando 10% de R${preco:.1f}, temos R${Aumentar(preco):.1f}")
print(f"Diminuindo 30% de R${preco:.1f}, temos R${Diminuir(preco, 30):.1f}")
print(f"O dobro de R${preco:.1f} vale R${Dobro(preco)}")
print(f"A metade de R${preco:.1f} vale R${Metade(preco)}")