def leiaInt(msg):
    n = 0

    while True:
        try:
            n = int(input(msg))
            
        except (ValueError):
            print("\033[1;31mOps, parece que tivemos um problema com o tipo de dados informados por você.Por favor, considere tentar novamente!\033[m")
        except (KeyboardInterrupt):
            print("\n\033[1;31mO usuário preferiu não informar os dados\033[m")
            return 0
        else:
            break

    return n


def leiaFloat(msg):
    n = 0

    while True:
        try:
            n = float(input(msg))

        except (NameError, ValueError): 
            print(f"\033[1;31mOps, parece que tivemos um problema com o tipo de dados informados por você.Por favor, considere tentar novamente\033[m")

        except (KeyboardInterrupt):
            print("\n\033[1;31mO usuário preferiu não informar os dados\033[m")
            return 0
        else:
            break

    return n