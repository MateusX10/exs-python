import random

alunos = ["Maria", "João", "Pedro", "Ana"]
random.shuffle(alunos)
print(f'O aluno escolhido foi {random.choice(alunos)}')
for pos in range(0, len(alunos)):
    print(f'{pos+1}º aluno: {alunos[pos]}')
