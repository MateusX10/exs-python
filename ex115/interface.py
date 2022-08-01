import os
from time import sleep

def line():
    print('-=' * 30)
def title(msg, tam=60):
    print('~' * 60)
    print(msg.center(tam))
    print('~' * 60)

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO!Por favor, digite um número inteiro válido!\033[m')
            continue
            print('...')
        except (KeyboardInterrupt):
            print('\n\033[1;31mO usuário preferiu não informar os dados\033[m')
            return 0
        else:
            return n
           

def menu(lst):
    title("MENU PRINCIPAL")
    c = 0
    while c < len(lst):
        print(f'\033[1;33m{c+1}\033[m - \033[1;32m{lst[c]}\033[m')
        c += 1
    escolha = leiaInt("\033[1;33mO que quer fazer?: \033[m")
    return escolha

