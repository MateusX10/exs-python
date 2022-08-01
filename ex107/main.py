from moeda import *


p = float(input('Preço: R$'))
print(f'O dobro de R${p:.2f} é R${dobro(p):.2f}')
print(f'A metade de R${p:.2f} é R${metade(p):.2f}')
print(f'Aumentando em 10%, temos R${aumento(p, 10):.2f}')
print(f'Diminuindo em 10%, temos R${diminuir(p, 10):.2f}')

