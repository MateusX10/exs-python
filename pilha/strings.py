def QuebraLinha(NumeroDeLinhas=1):
    '''==> Quebra linha na saída do programa
    :param NumeroDeLinhas: número de linhas a serem puladas
    :return: se retorno
    '''
    # Faz um for para realizar o devido número de quebras de linha
    for linha in range(0, NumeroDeLinhas):
        print("\n")


def linha(NumeroCaracteres=60):
    '''==> Exibe uma linha de cabeçalho 
    :param NumeroCaracteres: tamanho da linha
    :return: sem retorno
    '''
    print('-' * NumeroCaracteres)


def titulo(texto):
    '''==> Exibe uma mensagem em formato de título na tela 
    :param texto: texo a ser exibido na tela
    :return: sem retorno
    '''

    # Define tamanho das setas  do título
    tamanho = len(texto) + 4
     # Mostra linha
    linha(tamanho)
    # Mostra texto
    print(texto)
    linha(tamanho)


def menu():
    '''==> Mostra um menu na tela
    :return: sem retorno
    '''
    titulo('''\033[1;32mMenu: \n\n[ 1 ] - Empilhar \n[ 2 ] - Desempilhar \n[ 3 ] - Mostrar topo
[ 4 ] - Mostrar pilha inteira \n[ 5 ] - Sair\033[m
    ''')




