from pilhas import *
from time import sleep


EscolhaUsuario = 0;

# Cria a pilha de dados
pilha = CriaPilha(8)


# Loop infinito
while True:

    # Mostra o menu de opções na tela
    menu()

    # Faz input de dados do usuário e a validação
    while True:
        try:
            EscolhaUsuario = int(input("Sua escolha: "))
        except:
            print("\033[1;31mTivemos problemas com o tipo de dados que você informou.Tente novamente\033[m")
        else:
            break

    # Usuário optou por adicionar um valor à pilha
    if EscolhaUsuario == 1:
        pilha = Empilhar(pilha)

    # Usuário optou por remover o último elemento da pilha
    elif EscolhaUsuario == 2:
        pass

    # Usuário optou por mostrar o topo da pilha
    elif EscolhaUsuario == 3:
        MostraTopo(pilha)

    # Usuário optou por mostrar o conteúdo todo da pilha
    elif EscolhaUsuario == 4:
        pass

    # Usuário optou por sair do programa
    elif EscolhaUsuario == 5:
        print("Saindo...")
        sleep(1.5)
        break
    
    # Usuário informou uma opção inválida
    else:
        print("\033[1;31mOpção inválida.Por favor, tente novamente\033[m")


print("<<< Volte sempre! >>>")
