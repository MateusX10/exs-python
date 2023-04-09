# Faz o input de dados do usuário e a validação dos dados inseridos por ele
def leiaFloat(msg):
    ''' => Faz o input de dados do usuário e valida a entrada de dados do user
    :param msg: mensagem a ser mostrada ao usuário durante o input de dados
    :return: retorna a escolha do usuário
    '''
    EscolhaUsuario = 0
    while True:
        try:
            EscolhaUsuario = float(input(msg))
        except (ValueError, TypeError):
            print("\n\033[1;31mTivemos um problema com o tipo de dados que você informou.\033[m")

        except (KeyboardInterrupt):
            print("\n\033[1;31mO usuário preferiu não digitar esse número.\033[m")
            # 5 ==> o usuário sairá do loop
            return 5
        else:
            return EscolhaUsuario



# Faz o input de dados do usuário e a validação dos dados inseridos por ele
def leiaInt(msg):
    ''' => Faz o input de dados do usuário e valida a entrada de dados do user
    :param msg: mensagem a ser mostrada ao usuário durante o input de dados
    :return: retorna a escolha do usuário
    '''
    EscolhaUsuario = 0
    while True:
        try:
            EscolhaUsuario = int(input(msg))
        except (ValueError, TypeError):
            print("\n\033[1;31mTivemos um problema com o tipo de dados que você informou.\033[m")

        except (KeyboardInterrupt):
            print("\n\033[1;31mPara sair, selecione '5' no menu de opções.\033[m")
        else:
            return EscolhaUsuario


def leiaPilha():
    EscolhaUsuario = 0
    while True:
        try:
            EscolhaUsuario = int(input("Capacidade da pilha: "))
        except (ValueError, TypeError):
            print("\n\033[1;31mTivemos um problema com o tipo de dados que você informou.\033[m")

        except (KeyboardInterrupt):
            print("\n\033[1;31mPara sair, escolha o tamanho da pilha e selecione '5' no menu de opções\033[m")
        else:
            if EscolhaUsuario > 0:
                return EscolhaUsuario
            print("\n\033[1;31mCapacidade da pilha não pode ser nula\033[m")
            
