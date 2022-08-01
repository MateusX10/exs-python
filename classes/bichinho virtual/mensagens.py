from time import sleep


def MensagemInvalida(msg):
    print(f'\033[1;31m"\033[1;33m{msg}\033[1;31m" é uma resposta inválida!Tente novamente.\033[m')

def SimOuNao():
    print('\033[1;31mDigite somente "\033[1;33mS\033[1;31m" ou "\033[1;33mN" \033[m')

def RetomandoPerguntas():
    print('\033[1;33mRetomando perguntas...\033[m')
    sleep(1)


