def leiaInt(msg):
    global num
    num = ""
    while True:
        try:
            num = int(input(msg))
        except (ValueError, NameError):
            print(f'\033[1;31m"{num}" não é um valor válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[1;31mUsuário preferiu não informar os dados\033[m')
            quit()
        
        else:
            return num
