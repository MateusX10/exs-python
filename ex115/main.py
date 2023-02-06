from strings import *
from arquivos import *
import os
from time import sleep

if not os.path.isfile("arquivo.txt"):
    CriaArquivo("arquivo.txt")


    
while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar uma nova pessoa", "Sair do sistema"])



    if resposta == 1:
        title("\033[1;32mPessoas Cadastradas\033[m")
        LerArquivo("arquivo.txt")

    elif resposta == 2:
        title("\033[1;32mNovo Cadastro\033[m")
        EscreverArquivo("arquivo.txt")
        sleep(1.5)
    elif resposta == 3:
        print("Saindo do sistema...")
        sleep(1)
        break
        title(f"\033[1;34m{lista[resp - 1]}\033[m")

    else:
        print("\033[1;31mOpção inválida.Tente novamente.\033[m")



print("\033[1;33m <<< \033[1;32mvolte sempre \033[1;33m>>>")