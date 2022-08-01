from random import shuffle,choice


alunos = list()
for aluno in range(1,5):
    al = str(input(f'{aluno}º aluno: '))
    alunos.append(al)
shuffle(alunos)
print(choice(alunos))

