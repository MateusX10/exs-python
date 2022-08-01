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
           


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO!Digite um número real válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[1;31mO usuário preferiu não informar os dados\033[m')
            return 0
        else:
            return n

