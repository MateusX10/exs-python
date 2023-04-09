from pilhas import *
from strings import *
from time import sleep
from sistema_operacional import *
from numeros import leiaInt, leiaPilha
from arquivos import *



arquivo = "pilha.txt"

CriaArquivo(arquivo)

EscolhaUsuario = 0;

ComandoLimparTela = VerificaOSistemaOperacionalDoUsuario()

# Cria a pilha de dados com capacidade de 8 elementos

CapacidadeDaPilha = leiaPilha()
pilha = CriaPilha(CapacidadeDaPilha)


# Loop infinito
while True:

    # Mostra o menu de opções na tela
    menu()

    # Faz input de dados do usuário e a validação
    EscolhaUsuario = leiaInt("Sua escolha: ")
    
    QuebraLinha()
    #titulo(EscolhaUsuario)
    QuebraLinha()
    # Usuário optou por adicionar um valor à pilha
    if EscolhaUsuario == 1:
        pilha = Empilhar(pilha)

    # Usuário optou por remover o último elemento da pilha
    elif EscolhaUsuario == 2:
        pilha = Desempilhar(pilha)

    # Usuário optou por mostrar o topo da pilha
    elif EscolhaUsuario == 3:
        MostraTopo(pilha)

    # Usuário optou por mostrar o conteúdo todo da pilha
    elif EscolhaUsuario == 4:
        MostrarPilhaInteira(pilha)

    # Usuário optou por sair do programa
    elif EscolhaUsuario == 5:
        print("Saindo...")
        sleep(1.5)
        break
    
    # Usuário informou uma opção inválida
    else:
        print("\033[1;31mOpção inválida.Por favor, tente novamente\033[m")
    
    QuebraLinha()
    Pausa()
    LimpaTela(ComandoLimparTela)


print("<<< Volte sempre! >>>")