def leiaInt(msg):
    n = 0
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[1;31mTivemos um problema com o tipo de dados que você informou.\033[m")

        except (KeyboardInterrupt):
            print("\n\033[1;31mO usuário preferiu não digitar esse número.\033[m")
            return 3
        else:
            if 0 < n < 4:
                return n
            print(f"\033[1;31mERRO!Por favor, digite um número entre 1 e 3!\033[m")


def line(tam=60):
    print('-' * tam)


def title(phrase):
    print('\033[1m', end='')
    line()
    print(phrase.center(65))
    print('\033[1m', end='')
    line()


def menu(lista):
    resp = 0
    title("MENU")
    while True:
        c = 1
        for item in lista:
            print(f"\033[1;33m{c}\033[m - \033[1;32m{item}\033[m")
            c += 1
        resp = leiaInt("\033[1mSua escolha: ")        
        return resp

