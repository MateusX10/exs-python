def metade(p, formatado=True):
    res = p / 2
    return moedaa(res) if formatado else res


def dobro(p, formatado=True):
    res = p * 2
    return moedaa(res) if formatado else res


def aumento(p, percentual=10, formatado=True):
    ''' ==> Retorna o aumento de 10% de um preço
        :param p: preco a ser calculado
        :param percentual: porcentagem de aumento
        :param formatado: se o preço vai ou não ser formatado pela função moeda
        :return: retorna o preço formatado ou não a depender da escolha
'''
    res = p + (p * percentual / 100)
    return moedaa(res) if formatado == True else res

def diminuir(p, percentual=10, formatado=True):
    res = p - (p * percentual / 100)
    return res if formatado is True else res


def moedaa(p, simb='R$'):
    res = f'{simb}{p:.2f}'.replace(".", ",")
    return res

help(aumento)