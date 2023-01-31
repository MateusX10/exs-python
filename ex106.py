from time import sleep


def title(phrase, cor=0):
    length = len(phrase) + 3
    print(f"{cores[cor]}")
    print("~" * length)
    #print(phrase.center(length))
    print(f"  {phrase}")
    print('~' * length)
    print(cores[0])



QuestionUser = ' '

cores = ('\033[1;40m',
        '\033[1;41m', #vermelho
        '\033[1;42m', #verde
        '\033[1;43m', # amarelo
        '\033[1;44m', #azul
        '\033[1;45m', #roxo
        '\033[1;46m',
        '\033[1;47m', #cinza
            ) #ciano


while True:
    title("SISTEMA DE AJUDA PyHELP", 1)
    QuestionUser = str(input("\033[m \033[1mFunção ou biblioteca > ")).strip().lower()
    if QuestionUser.upper() == 'FIM':
        break
    #print(f"\033[1;34;42mAcessando o manual do comando \033[1;33m{QuestionUser}\033[1;32m,...")
    title(f"Acessando o manual do comando '{QuestionUser}'", 2)
    sleep(3)
    try:
        print(f'{cores[6]}', end='')
        help(QuestionUser)
        print(f"{cores[0]}", end='')
    except:
        print("\033[1;41mOps, comando não encontrado!Considere tentar novamente!")

    
title("Volte sempre!", 3)