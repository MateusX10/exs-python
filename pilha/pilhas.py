from numeros import *


#cria a pilha
def CriaPilha(NumeroElementos=5):
    '''=> Cria uma pilha de dados
    :param NumeroElementos: número total de elementos que terá na pilha (o limite de tamanho)
    :return: retorna a pilha de dados
    '''

    # pilha de dados
    pilha = {"elementos": [], "capacidade da pilha": NumeroElementos, "total de elementos": 0}
    
    return pilha


def menu():
    print('''Menu: \n\n[ 1 ] - Empilhar \n[ 2 ] - Desempilhar \n[ 3 ] - Mostrar topo
[ 4 ] - Mostrar pilha inteira \n[ 5 ] - Sair
    ''')


# Adiciona elementos a pilha
def Empilhar(p):
    '''=> Adiciona elementos a pilha
    :param p: a pilha de dados a ser modificada
    :return: retorna a pilha atualizada para o arquivo principal    
    '''

    pilha = p

    NovoElementoDaPilha = leiaFloat("Valor a ser inserido na pilha: ")

    pilha["elementos"].append(NovoElementoDaPilha)
    
    pilha["total de elementos"] += 1

    return pilha



# Mostra o último elemento inserido na pilha
def MostraTopo(p):
    '''=> Mostra o último elemento inserido na pilha
    :param p: a pilha de dados
    :return: sem retorno
    '''

    # Imprime na tela o topo da pilha
    print(f"Topo => {p['elementos'][-1]}")






