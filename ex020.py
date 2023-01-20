from random import shuffle


alunos = ["Maria", "Pedro", "José", "Fernanda"]

shuffle(alunos)


print(f'A ordem de apresentação será: ')

for pos, aluno in enumerate(alunos):
    print(f'{pos + 1} - {aluno}')
