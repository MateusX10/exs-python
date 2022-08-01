# US$dólar = R$4.80
dinheiro = float(input('Quanto dinheiro você tem na carteira? R$'))
print(f'R${dinheiro:.2f}')
dólar = dinheiro / 4.80
euro = dinheiro / 5.27
iene = dinheiro / 0.039
print(f'''Com R${dinheiro:5.2f}, você pode comprar:
US${dólar:5.2f};
£{euro:5.2f}
¥{iene:5.2f}
''')
