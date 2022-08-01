'''Crie um programa que simule um supermercado.O programa vai precisar
ter uma lista de produtos e uma espécie de lista de clientes.Cada um
somente comprará produtos que comecem com a primeira letra de seus
nomes.
e

Ex: uma pessoas chamada "Carian" somente comprará produtos que comecem
com a letra "C", como Chocolate, coco, cano etc...

- Caso algum cliente comece com uma letra na qual na tenha nos produtos
do supermercado, essa pessoa tem o direito de comprar um produto 
qualquer por 30% de desconto

Dica: use a função .startswith()
'''

produtos = ["Amora", "arroz", "água sanitária", "abóbora", "bola",
"brócolis", "brinquedo", "bolacha", "coco", "carne", "canela", "doces",
"damasco", "espinafre", "ervilha", "farinha", "feijão", "goiaba",
"galinha", "hortelã", "iogurte", "jabuticaba", "kiwi", "lápis",
"macarrão", "miojo", "melanca", "mamão", "nachos", "oden", "pimenta",
"pinhão", "pêssego", "quibe", "rabanete", "sorverte", "salame",
"tapioca", "uva"]

nomes = ["Ana", "Brian", "Carian", "Davi", "Eric", "Fernando", 
"Gabriel", "Hércules", "Ionara", "João", "Káren", "Larissa", "Mateus",
"Nicolas", "Omar", "Paulo", "Quelli", "Ricardo", "Satoshi", "Totoro",
"Ui", "Vinícios", "Wanessa", "Xian", "Yuki", "Zenilson"]

for produto in produtos:
    print(produto)

for nome in nomes:
    print(nome)


for pos, nome in enumerate(nomes):
    print(f'\033[1;34m=== CLIENTE{pos+1} ===\033[m')
    for pos, produto in enumerate(produtos):
        if produto.upper().startswith(nome[0].upper()):
            print(f'{nome} comprou {produto}')
            break
        if produto == produtos[-1]:
            from random import choice
            escolha = 0
            print(f'''\033[1;31m{nome} não encontrou um produto com seu nome,
logo terás de ofertar 30% de desconto a ele na compra de um produto
qualquer\033[m''')
            escolha = choice(produtos)
            print(f'''\033[1;32m{nome} recebeu 30% de desconto na compra de um
{escolha}\033[m''')
