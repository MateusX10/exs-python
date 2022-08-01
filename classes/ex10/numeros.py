def leiaInt(msg):
        while True:
            try:
                v = int(input(msg))
            except (ValueError, NameError):
                print('\033[1;31mTivemos um problema com o tipo de dados que você digitou.\033[m')
            else:
                return v

def leiaFloat(msg):
    try:
        valor = float(input(msg))
    except (NameError, ValueError):
        print('\033[1;31mTivemos um problema com o tipo de dados que você digitou\033[m')
    else:
        return valor

