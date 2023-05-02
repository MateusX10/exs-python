def leiaInt(msg: str) -> int:
    '''==> Valida a entrada de dados do tipo inteiro do usuário
        :param msg: mensagem a ser mostrada ao usuário durante o "input" de dados
        :return: Retorna o valor resultante da entrada de dados do usuário
    '''

    while True:
        try:
            valor = int(input(msg))

        except (ValueError, NameError, TypeError):
            print(f"\033[1;31m Tivemos um problema com o tipo de dados que você informou\033[m")

        else:
            return valor
        
# Valida a entrada de dados do tipo ponto flutuante do usuário
def leiaFloat(msg: str) -> float:
    '''==> Valida a entrada de daqdos do tipo ponto flutuante do usuário
        :param msg: mensagem a ser mostrada ao usuário durante o input de dados do usuário
        :return: retorna o valor resultante da entrada de dados do usuário
        '''
    while True:
        try:
            valor = float(input(msg))

        except (ValueError,NameError,TypeError):
            print("\033[1;31mTivemos um problema com o tipo de dados que você informou\033[m")

        else:
            return valor

