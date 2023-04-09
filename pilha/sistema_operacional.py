from os import name, system


def VerificaOSistemaOperacionalDoUsuario():
    ComandoDeLimparTela = " "
    if name == "posix":
        ComandoDeLimparTela = "clear"

    elif name == "nt":
        ComandoDeLimparTela = "cls"

    return ComandoDeLimparTela


def LimpaTela(comando):
    system(f"{comando}")


def Pausa():
    input("Pressione qualquer tecla para continuar...")
        


