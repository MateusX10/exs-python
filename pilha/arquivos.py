def CriaArquivo(arqname):
    try:
        arquivo = open(arqname, "a+")


    except:
        print(f"\033[1;31mOcorreu um erro ao criar o arquivo  '{arqname}'!\033[m")
        quit()

    else:
        pass