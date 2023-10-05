def leiaString(string) -> str:
    '''--> Pega  uma string e a valida
        Parâmetros:
            String: string a ser validada
            :return: retorna a string validada

    '''

    from sys import exit

    while True:
        try:
            usuario = str(input(string))

        except (KeyboardInterrupt):
            print("\033[1;31mEntrada de dados interrompida pelo usuário.\033[m")
            exit(1) #informa ao S.O que houve algum tipo de erro durante a execução  #do programa

        else:
            if usuario.strip() == '':
                print("\033[1;31mPor favor, digite uma string válida!\033[m")
                continue
            
            return usuario

