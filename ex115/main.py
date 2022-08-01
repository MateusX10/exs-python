from interface import *
from arquivo import *
from time import sleep

arq = "texto.txt"
if not ArquivoExiste(arq):
    CriarArquivo(arq)
opcs = ["Ver Pessoas Cadastradas", "Cadastrar Uma Nova Pessoa", "Sair Do Sistema"]
while True:
    escolha = menu(opcs)
    if escolha == 1:
        title(f'\033[1;34m{opcs[escolha-1]}\033[m')
        sleep(1)
        VerPessoas(arq)
    elif escolha == 2:
        title(f'\033[1;34m{opcs[escolha-1]}\033[m')
        sleep(1)
        Cadastrar(arq)
    elif escolha == 3:
        title(f'\033[1;34m{opcs[escolha-1]}\033[m')
        print("SAINDO...")
        sleep(1)
        break
    else:
        print('\033[1;31mERRO!Digite uma opção válida!\033[m')

print('\033[1;35m<<< Volte sempre! >>>\033[m')