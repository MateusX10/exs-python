# Faz o input de dados do usuário e a validação dos dados inseridos por ele
def leiaFloat(msg):
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
            print("\n\033[1;31mO usuário preferiu não digitar esse número.\033[m")
            # 5 ==> o usuário sairá do loop
            return 5
        else:
            return EscolhaUsuario