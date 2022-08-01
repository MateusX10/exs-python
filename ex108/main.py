from moeda import *


p = float(input('Preço: R$'))
print(f'O dobro de {moedaa(p)} é {moedaa(dobro(p))}')
print(f'A metade de {moedaa(p)} é {moedaa(metade(p))}')
print(f'Aumentando em 10%, temos {moedaa(aumento(p, 10))}')
print(f'Diminuindo em 10%, temos {moedaa(diminuir(p, 10))}')

