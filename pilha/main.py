from pilhas import *
from strings import *
from time import sleep
from sistema_operacional import *
from numeros import leiaInt, leiaPilha
from arquivos import *


# Nome do arquivo 
arquivo = "pilha.txt"

# Cria arquivo "pilha.txt"
CriaArquivo(arquivo)

EscolhaUsuario = 0;

# Verifica o S.O do user e retorna o comando binário do S.O de limpar a tela
ComandoLimparTela = VerificaOSistemaOperacionalDoUsuario()

# Define a capacidade da pilha
CapacidadeDaPilha = leiaPilha()

# Cria a pilha com "x" capacidade
pilha = CriaPilha(CapacidadeDaPilha)

# Opções de escolha do usuário
opcs = ["Adicionar valor", "exluir valor", "mostrar topo", "mostrar pilha", "sair"]

# Loop infinito
while True:

    # Mostra o menu de opções na tela
    menu()

    # Faz input de dados do usuário e a validação
    EscolhaUsuario = leiaInt("Sua escolha: ")
    
    QuebraLinha()
    # Mostra em formato de título a escolha do user
    titulo(f'  {opcs[EscolhaUsuario-1]}')
    sleep(0.7)
    QuebraLinha()
    # Usuário optou por adicionar um valor à pilha
    if EscolhaUsuario == 1:
        pilha = Empilhar(pilha)
        # Subscreve o arquivo .txt com as alterações feitas na pilha
        EscreveNoArquivo(arquivo, pilha["elementos"])
    # Usuário optou por remover o último elemento da pilha
    elif EscolhaUsuario == 2:
        pilha = Desempilhar(pilha)
        # Subscreve o arquivo .txt com as alterações feitas na pilha
        EscreveNoArquivo(arquivo, pilha["elementos"])
    # Usuário optou por mostrar o topo da pilha
    elif EscolhaUsuario == 3:
        MostraTopo(pilha)

    # Usuário optou por mostrar o conteúdo todo da pilha
    elif EscolhaUsuario == 4:
        MostrarPilhaInteira(pilha)

    # Usuário optou por sair do programa
    elif EscolhaUsuario == 5:
        # Apaga conteúdo da pilha antes de encerrar o programa
        LimpaConteudoDaPilha(arquivo, pilha["elementos"])
        print("Saindo...")
        sleep(1.5)
        break
    
    # Usuário informou uma opção inválida
    else:
        print("\033[1;31mOpção inválida.Por favor, tente novamente\033[m")
    
    QuebraLinha()
    Pausa()
    # Limpa a tela com o comando binário de limpar tela do S.O do user
    LimpaTela(ComandoLimparTela)


print("\n\n<<< Volte sempre! >>>")