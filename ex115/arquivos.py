from strings import title



def CriaArquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, "a+")

    except: 
        print(f"\033[1;31mNão foi possivel criar o arquivo\033[m")

    else:
        print(f"\033[1;32mArquivo {nome_arquivo} criado com sucesso")

    finally:
        arquivo.close()


def LerArquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, "r")

    except (FileNotFoundError):
        print("\033[1;31mNão foi possível ler o arquivo\033[m")

    else:
        for l in arquivo:
            dado_formatado = l.split(";")
            print(f"{dado_formatado[0]:<30}{dado_formatado[1]:>5}", end='')

    finally:
        arquivo.close()


def EscreverArquivo(nome_arquivo):
    nome = ''
    idade = 0
    try:
        arquivo = open(nome_arquivo, "a")

    except:
        print(f"\033[1;31mNão foi possível escrever no arquivo.\033[m")

    else:
        nome = str(input("Nome: ")).strip().capitalize()
        idade = int(input("Idade: "))
        try:
            arquivo.write(f"{nome};{idade} anos\n")
        except:
            print("\033[1;31mOcorreu um erro ao escrever no arquivo...\033[m")
        else:
            title(f"\033[1;32mNovo cadastro de {nome} efetivado com sucesso!\033[m")
    finally:
        arquivo.close()


