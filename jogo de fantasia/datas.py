def RetornaDataAtual() -> str:
    '''==> Retorna a data atual
        :return: retorna a data atual formatada
    '''
    from datetime import datetime

    data_atual = datetime.today()
    
    data_formatada = data_atual.strftime("%d/%m/%Y")
    print(type(data_formatada))
    return (data_formatada)

