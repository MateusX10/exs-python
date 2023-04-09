def QuebraLinha(NumeroDeLinhas=1):
    for linha in range(0, NumeroDeLinhas):
        print("\n")


def linha(NumeroCaracteres=60):
    print('-' * NumeroCaracteres)


def titulo(texto):
    tamanho = len(texto) + 4
    linha(tamanho)
    print(texto)
    linha(tamanho)


def menu():
    linha()
    titulo('''Menu: \n\n[ 1 ] - Empilhar \n[ 2 ] - Desempilhar \n[ 3 ] - Mostrar topo
[ 4 ] - Mostrar pilha inteira \n[ 5 ] - Sair
    ''')
    linha()
