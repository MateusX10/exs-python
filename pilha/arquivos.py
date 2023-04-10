def CriaArquivo(arqname):
    '''==> Cria arquivo 'pilha.txt' que conterá a pilha de dados
    :param arqname: nome do arquivo
    :return: sem retorno
    '''

    # Tenta criar o arquivo
    try:
        arquivo = open(arqname, "a+")

    # Arquivo não pode ser criado devido a um erro
    except:
        print(f"\033[1;31mOcorreu um erro ao criar o arquivo  '{arqname}'!\033[m")

    # Arquivo criado com sucesso
    else:
        pass
    
    # Fecha arquivo
    finally:
        arquivo.close()



def EscreveNoArquivo(arqname, p):
    '''==> Escreve/subscreve o arquivo 'pilha.txt' com as novas modificações da pilha
    :arqname: nome do arquivo da pilha de dados
    :p: pilha de dados
    '''

    # Tenta abrir o arquivo
    try:
        arquivo = open(arqname, "w")

    # Não foi possível abrir o arquivo devido a um erro
    except:
        print("\033[1;31mOcorreu um erro ao abrir o arquivo para escrita \033[m")

    # Arquivo aberto com sucesso
    else:
        # Tenta escrever/subscrever o arquivo
        try:
            arquivo.write(f"{p}")

        # Não foi possível realizar a escrita no arquivo
        except:
            print("\033[1;31mOcorreu um erro ao escrever no arquivo 'pilha.txt'\033[m")
        
        # Fecha arquivo
        finally:
            arquivo.close()
        

def LimpaConteudoDaPilha(arqname, p):
    '''==> Zera o conteúdo da pilha
    :arqname: nome do arquivo da pilha
    :p: pilha de dados a ser manipulada
    :return: sem retorno
    '''

    # Tenta abrir o arquivo
    try:    
        arquivo = open(arqname, "a")

    # Ocorreum um erro ao abrir o arquivo
    except:
        print("\033[1;31mOcorreu um erro ao abrir o arquivo\033[m")

    # O conteúdo do arquivo é excluído
    else:
        arquivo.truncate(0)