def line(tam=60):
    print(tam * '-')


def title(msg, tam=60):
    print('-' * tam)
    print(msg.center(tam))
    print('-' * tam)

def Aumentar(p, percentual=10, formata=True):
    ''' --> Retorna o percentual de aumento de um produto
    :param p: preço a ser calculado o percentual
    :param percentual: percentual a ser acrescentado no produto
    :param formata: formatar ou não o resultado
    :return: retorna o resultado em percentual (formatado ou não)
    '''
    resultado =  (p + (p * percentual / 100))
    return moedas(resultado) if formata else resultado
    

def Diminuir(p, percentual=10, formata=True):
    ''' --> Retorna o percentual de redução do produto
    :param p: preço a ser calculado o percentual
    :param percentual: percentual a diminuir do produto
    :param formata: formatar ou não o resultado
    :return: retorna o resultado em percentual (formatado ou não)
    '''
    resultado = (p - (p * percentual / 100))
    return moedas(resultado) if formata else resultado

def Dobro(p, formata=True):
    ''' --> Retorna o dobro do valor do produto
    :param p: preço do produto
    :param formata: formatar ou não o resultado
    '''
    resultado = (p * 2)
    return moedas(resultado) if  formata else resultado

def Metade(p, formata=True):
    ''' --> Retorna a metade do valor do produto
    :param p: preço do produto a ser calculado
    :param formata: formatar ou não o resultado final
    '''
    resultado  = (p / 2)
    return moedas(resultado) if formata else resultado


def moedas(p, formata=True):
    ''' --> Formata um valor em moeda brasileira
    :param p: preço a ser formatado
    :param formata: formatar ou não o preço do produto
    '''
    if formata:
        resultado = f"R${p:.2f}".replace(".", ",")
    else:
        resultado = p
    return resultado


def resumo(value, aumento, reducao):
    '''--> Retorna o resumo do valor
    :param value: preço a ser mostrado
    :param aumento: percentual de aumento do produto
    :param reducao: percentual de redução do produto

    '''
    title("RESUMO DO VALOR", 40)

    print(f'''Preço analisado: \t{moedas(value)}
Dobro do preço: \t{Dobro(value)}
Metade do preço: \t{Metade(value)}
{aumento}% de aumento: \t{Aumentar(value, 10)}
{reducao}% de redução: \t{Diminuir(value, 12)}  
            ''')
    line(40)
