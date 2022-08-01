from moeda import *


p = float(input('Preço: R$'))
print(f'O dobro de {moedaa(p)} é {dobro(p, False)}')
print(f'A metade de {moedaa(p)} é {metade(p)}')
print(f'Aumentando em 10%, temos {aumento(p, 10)}')
print(f'Diminuindo em 10%, temos {diminuir(p, 10)}')

