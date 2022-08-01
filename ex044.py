print(f'\033[1;32m{" LOJAS TINNY :D ":=^50} \033[30m')
preço = float(input('Preços das compras: R$'))
print('''\033[1;33mFORMAS DE PAGAMENTO: 
[ 1 ] - À vista dinheiro/cheque
[ 2 ] - À vista cartão
[ 3 ] - 2x no cartão
[ 4 ] - 3x ou mais no cartão
\033[m''')
while True:
    choice = int(input('Qual a sua escolha? '))
    if  5 > choice > 0:
        break
    print('\033[1;31mERRO!Digite uma opção válida!\033[m')
if choice == 1:
    novo = preço - (preço * 10 / 100)
elif choice == 2:
    novo = preço - (preço * 5 / 100)
elif choice == 3:
    novo = preço
else:
    novo = preço + (preço * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    print(f'Sua compra foi parcelada em {parcelas}x de {novo/parcelas:.2f} COM JUROS')
print(f'Sua compra de R${preço:5.2f} no final vai custar R${novo:5.2f}')
