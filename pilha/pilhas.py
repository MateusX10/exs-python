from numeros import leiaFloat


#cria a pilha
def CriaPilha(NumeroElementos=5):
    '''=> Cria uma pilha de dados
    :param NumeroElementos: número total de elementos que terá na pilha (o limite de tamanho)
    :return: retorna a pilha de dados
    '''

    # pilha de dados
    pilha = {"elementos": [], "capacidade da pilha": NumeroElementos, "total de elementos": 0}
    
    return pilha



def PilhaEstaVazia(p):
    '''==> Verifica se a pilha está vazia 
    :param p: pilha de dados a ser verificada
    :return: informa se a pilha está vazia ou não
    '''
    if p["total de elementos"] == 0:
        return True
    else:
        return False


def PilhaEstaCheia(p):
    '''==> Verifica se a pilha está cheia 
    :param p: pilha de dados a ser verificada
    :return: informa se a pilha está cheia
    '''
    if p["total de elementos"] == p["capacidade da pilha"]:
        return True

    else:
        return False

# Adiciona elementos a pilha
def Empilhar(p):
    '''=> Adiciona elementos a pilha
    :param p: a pilha de dados a ser modificada
    :return: retorna a pilha atualizada para o arquivo principal    
    '''

    if PilhaEstaCheia(p):
        print("\033[1;31mOps, pilha cheia!\033[m")

    else:


        NovoElementoDaPilha = leiaFloat("Valor a ser inserido na pilha: ")

        p["elementos"].append(NovoElementoDaPilha)
        
        p["total de elementos"] += 1

        print(f"\n\n\033[1;32mValor {NovoElementoDaPilha} adicionado com sucesso!\033[m")

    return p


def Desempilhar(p):
    '''==> Remove um item da pilha
    :param p: pilha de dados a ser verificada
    :return: retorna a pilha atualizada com o elemento já retirado
    '''

    if PilhaEstaVazia(p):
        print("\033[1;31mPilha vazia\033[m")

    else:
        # Armazena o valor antes de ser removido
        cache = p['elementos'][-1]
        p["elementos"].pop()
        p["total de elementos"] -= 1

        print(f"\033[1;32mValor {cache} removido da pilha com sucesso!\033[m")

    return p


# Mostra o último elemento inserido na pilha
def MostraTopo(p):
    '''=> Mostra o último elemento inserido na pilha
    :param p: a pilha de dados
    :return: sem retorno
    '''

    if PilhaEstaVazia(p):
        print("\033[1;31mPilha vazia\033[m")

    else:

        # Imprime na tela o topo da pilha
        print(f"Topo => {p['elementos'][-1]}")


def MostrarPilhaInteira(p):
    '''==> Exibe a pilha de dados inteira
    :param p: pilha de dados a ser exibida
    :return: sem retorno
    '''
    if PilhaEstaVazia(p):
        print("\033[1;31mPilha vazia\033[m")
    else:
        # Armazena o número total de itens da pilha
        TotalDeElementosDaPilha = p["total de elementos"]
        print("Pilha => [", end='')
        # Faz um laço for que exibe a pilha de dados na tela
        for posicao, ElementoDaPilha in enumerate(p["elementos"]):
            print(f"{ElementoDaPilha}, " if posicao + 1 < TotalDeElementosDaPilha else f"{ElementoDaPilha}", end='')
        print("]\n")





