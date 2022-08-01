compras = ["macarrão", "mortaledela", "pão", "chocolate",
"barra de chocolate", "Jabuticaba"]
nomes = ["Maria","Mateus", "Mariana", "Marco", "João", "Joana",
"Julia", "Jaqueline", "Fernando", "Larissa"]

comeca_com_j_compra = comeca_com_j_nome = False
cont_j_compra = cont_j_nome = 0

for compra in compras:
    print(f'Compra atual: {compra}')
    if compra.startswith("choco") or compra.startswith("barra"):
        print('É do Mateus!')
    if compra.lower().startswith("j"):
        comeca_com_j_compra = True
        cont_j_compra += 1
    else:
        print('É para todos')


for nome in nomes:
    if nome.startswith("M") or nome.startswith("m"):
        print(f'{nome} é da família do Mateus :D')

    if nome.lower().startswith("j"):
        comeca_com_j_nome = True
        cont_j_nome += 1

    elif nome.startswith("J") or nome.startswith("j"):
        print(f'{nome} é da família do João ._.')

    else:
        print(f'{nome} é de família rival, favor ignorá-lo ):')

if comeca_com_j_compra:
    if cont_j_compra > 1:
        print('Há mais de uma palavra em compras que começa com "j"')
    else:
        print('Há uma palavra em compras que começa com "j"')

if comeca_com_j_nome:
    if cont_j_nome > 1:
        print('Há mais de uma palavra em nomes que começa com "J"')
    else:
        print('Há uma palavra em nomes que começa com "j"')

print('\033[33m-=' * 30)
for valor in nomes:
    if valor.upper().startswith("J"):
        print(f'começa com "J"')
else:
    print(f'Não começa com "J"')

print('\033[34m-=' * 30)
for cont in range(0,10):
    if cont <= 5:
        print('Não é maior do que 5')
else:
    print('É maior do que 5')

print('\033[1;34m-=' * 30)
for nome in nomes:
    if nome.upper().startswith("M"):
        print('Começa com M')
else:
    print('Não existe palavra com M')