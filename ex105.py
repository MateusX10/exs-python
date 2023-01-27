def notas(*num, sit=False):
    '''
    --> Analisa as notas de um aluno, retornando o boletim dos mesmos
    :param num: uma ou mais notas do aluno
    :param sit: situação do aluno
    :return: retorna boletim com as notas do aluno

    '''
    maior = menor = media = soma = 0
    notas = dict()
    for pos, v in enumerate(num):
        if pos == 0:
            maior = menor = v

        else:
            if v > maior:
                maior = v
            if v < menor:
                menor = v
        
        soma += v

    
    notas["quantidade de notas"] = len(num)
    notas["maior nota"] = maior
    notas["menor nota"] = menor
    media  = soma / notas["quantidade de notas"]
    notas["média"] = float(f"{media:.1f}")
    if sit:
        if notas["média"] >= 7 and notas["média"] <= 10:
            notas["situação"] = "aprovado"

        elif notas["média"] >= 5:
            notas["situação"] = "recuperação"

        elif notas["média"] < 5:
            notas["situação"] = "reprovado"

    return notas


boletim = notas(4, 5.5, 4, 4.2 , sit=True)

print(f"Boletim do aluno: {boletim}")

help(notas)