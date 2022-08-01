def leiaInt(msg):
    n = 0
    while True:
        try:
            n = int(input(msg))
        except (ValueError, NameError):
            print('\033[1;31mDados inválidos.Tente novamente\033[m')

        else:
            return n

def ZeroaEsquerda(num):
    return "0"+str(num)
