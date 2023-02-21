from os import system


def LimpaTela(msg=True):
    if msg:
        continuar = str(input("\nPressione 'ENTER' para continuar"))
    system("clear")


def leiaInt(msg1):
    while True:
        try:
            n = int(input(msg1))

        except:
            print("\033[1;31mOcorreu um erro.Por favor, tente novamente.\033[m")

        else:
            return n


def title(msg):

    print("-=" * 30)
    print(msg.center(60))
    print('-=' * 30)


def Menu(opcs):
    while True:
        print('\nSuas opções: ')
        for pos, valor in enumerate(opcs):
            print(f"[ {pos+1} ] - {valor}")
        print("\033[m")
        try:
            user = int(input("O que você deseja fazer? "))

        except:
            print("\033[1;31mOps, parece que ocorreu um erro!Por favor, tente novamente.\033[m")
            LimpaTela()

        else:
            if user <= len(opcs):
                title(f"\033[1;34m{opcs[user - 1]}\033[m")
                return user
            print(f"\033[1;31mDigite um valor entre 1 e {len(opcs)}\033[m")


def AdicionaItemNaFila(fila, tamanho_fila):
    if len(fila) != tamanho_fila:
        fila.append(leiaInt("Qual valor deseja adicionar a fila? "))
        print(f"\033[1;32mItem '{fila[-1]}' adicionado ao final da fila com sucesso!\033[m")
        return fila[-1]
    else:
        print("\033[1;33mOps, fila cheia!\033[m")


def ListaElementosDaFila(fila):
    if len(fila) == 0:
        print("\033[1;33mFila vazia\033[m")
    else:
        for pos, elemento in enumerate(fila):
            if pos != (len(fila) - 1):
                print(f"{elemento} --> ", end='')

            else:
                print(f'{elemento}\n')


def RemoveItensDaFila(fila):
    while True:
        if len(fila) == 0:
                print("\033[1;33mFila vazia\033[m")
                return False
        else:
            cache = fila[-1]
            fila.pop()
            print(f"\033[1;32mItem {cache} removido com sucesso\033[m")
            return True
            

