def ArquivoExiste(a):
    try:
        a = open(a, "rt")
    except (FileNotFoundError):
        return False
    else:
        return True


def CriarArquivo(a):
    try:
        arq = open(a, "wt+")
    except:
        print('\033[1;31mErro ao criar o arquivo\033[m')
    else:
        print(f'\033[1;32mArquivo {a} criado com sucesso!\033[m')
    finally:
        arq.close()

def Cadastrar(a):
    try:
        arq = open(a, "at")
    except:
        print('\033[1;31mOcorreu um erro ao abrir o arquivo\033[m')
    else:
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        arq.write(f'{nome};{idade}\n')
        print(f'\033[1;32mNovo Cadastro de {nome} realizado com sucesso!\033[m')
    finally:
        arq.close()

def VerPessoas(a):
    try:
        arq = open(a, "rt")
    except:
        print('\033[1;31mErro ao ler o arquivo\033[m')
    else:
        for linha in arq:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f'{dado[0]:<20}\t\t\t\t{dado[1]} anos')
    finally:
        arq.close()