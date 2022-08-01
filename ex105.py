def notas(*valores, sit=False):
    ''' ==> Mostra as informações referentes a nota do aluno e sua situação
        :valores: notas do aluno
        :sit: situação do aluno
        :return: retorna as notas do aluno e sua situação
    '''
    alunos = dict()
    alunos["tot"] = len(valores)
    alunos["maior"] = max(valores)
    alunos["menor"] = min(valores)
    alunos["média"] = sum(valores) / alunos["tot"]
    if sit:
        if alunos["média"] >= 7:
            alunos["situação"] = "BOA"
        elif alunos["média"] >= 5:
            alunos["situação"] = "RECUPERAÇÃO"
        else:
            alunos["situação"] = "RUIM"

    return alunos



r = notas(7, 5, 5, sit=True)
print(r)
help(notas)