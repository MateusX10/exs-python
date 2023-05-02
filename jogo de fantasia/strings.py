def FormataCor(cor: str) -> str:
    '''==> Retorna a cor em código escape ANSI em RGB
        :param cor: cor a ser atribuída ao texto (vermelho, verde, azul)
        :return: retorna a cor formatada em RGB
    '''
    cores = {"vermelho": "\033[1m\033[48;2;128;0;0m",  "verde": "\033[1m\033[48;2;0;128;0m",
             "azul": "\033[1m[\033[48;2;0;0;128m"}
    
    return cores[cor]


def linha(tamanho: int = 60) -> None:
    '''
    Imprime uma linha na tela
    :param tamanho int: tamanho da linha a ser imprimida
    :return: sem retorno
    '''
    print('-=' * tamanho)


def titulo(msg: str, cor: str) -> None:
    '''==> Imprime um título na tela
        :param msg: mensagem do título a ser mostrada
        :param cor: cor do texto do título emk RGB
        :return: sem retorno     
    '''
    tamanho = len(msg) + 2
    print(FormataCor(cor))
    linha(tamanho)
    print(msg.center(tamanho * 2))
    linha(tamanho)
    print("\033[0m")


