def mensagem():
    '''Exibe mensagem de despedida ("volte sempre") para o usuário
    :return: sem retorno
'''

    global sair
    print('\n\033[1;32m<<< \033[1;34mVolte quando puder :D \033[1;32m>>>\033[m')
    sair = True

def titulo(txt, caracter=30):       #Exibe título na tela
    ''' ===> Escreve um título no tela
        :txt: título a ser exibido
        :caracter: quantidade de caracter para destacar o título
        :return: sem retorno
'''
    print("\033[1;35m-=\033[m" * caracter)
    print(txt)
    print("\033[1;35m-=\033[m" * caracter)

def verifica():
    ''' ===> Verifica se a variável "sair" é True ou False, logo saindo do programa se True
    	:return: retorna True com o objetivo de sair (break) do laço de repetição While
    '''
    if sair:
        return True


sair = False
titulo("\033[1;33mJogo do Par Ou Ímpar\033[m".center(60))

while True:
    while True:
        if verifica():
            break
            
        try:
            num = int(input("\033[1;30mMe diga um número: "))
        except (ValueError, NameError): #mensagem de erro por tipo de dado digitado
            print("\033[1;31mOps!Tivemos um problema com o tipo de dados que você digitou.\nTente novamente\033[m")
        except (KeyboardInterrupt):
            mensagem() #dá mensagem de "volte sempre" ao usuário
        else:
            break
    if verifica():
        break

    if num % 2 == 0: #Verifica se  um número é par ou ímpar
        print(f"\033[1;32mO número {num} é \033[1;34mPAR\033[m")
    else:
        print(f'\033[1;32mO número {num} é \033[1;36mIMPAR\033[m')

    while True: # Este é o while do "deseja jogar novamente? " que vai ficar num looping caso o 
        try:  #usuário não informe os dados corretamente
            r = str(input("\033[1mDeseja jogar novamente? [S/N] ")).strip().upper()[0]

        except:
            print('\n') # Quebra linha para evitar poluição visual
            titulo("\033[1mPor favor, digite apenas \033[1;32m'S'\033[m ou  \033[1;31m'NÃO'\033[m")
            continue # joga direto pro laço

        else:
            if r in "SN": #Aqui, o usuário digitou "SIM" (S) ou "NÃO" (N) e dependendo da resposta
                break #ele vai convinuar jogando ou sair do jogo
            print("\033[1;33mOps!Digite somente \033[1;32m'S'\033[m \033[33mou \033[1;31m'NÃO'\033[m, beleza?")

    if r == "N": # Aqui, o usuário digitou "NÃO" (N), logo sairá do jogo
        mensagem() # Mensagem de "volte sempre" antes de sair do jogo

