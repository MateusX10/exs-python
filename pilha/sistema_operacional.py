from os import name, system


def VerificaOSistemaOperacionalDoUsuario():
    '''Verifica qual o S.O do user (windows, linux)
    :return: retorna o comando binário do S.O para limpar tela
    '''
    ComandoDeLimparTela = " "
    # O S.O é linux
    if name == "posix":
        # Comando bin que limpa a tela no linux
        ComandoDeLimparTela = "clear"
    # O S.O é windows
    elif name == "nt":
        # Comando bin que limpa a tela no windows
        ComandoDeLimparTela = "cls"

    return ComandoDeLimparTela


def LimpaTela(comando):
    '''==> Limpa a tela do programa
    :return: sem retorno
    '''
    # Limpa programa
    system(f"{comando}")



def Pausa():
    '''==> Pausa a execução do programa
    :return: sem retorno
    '''
    input("Pressione qualquer tecla para continuar...")
        


