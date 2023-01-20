alunos = []
aluno = []
soma = media = cont = soma =  0

while True:
    continuar = False
    r = ' '
    aluno.append(str(input("Nome: ")))
    aluno.append([float(input("Nota 1: ")), float(input("Nota 2: "))])
    soma += (aluno[-1][0] + aluno[-1][-1])
    aluno.append(soma / 2)
    alunos.append(aluno[:])
    aluno.clear()
    soma = 0
    while not continuar:
        r = str(input("Continuar [S/N]? ")).strip().upper()[0]
        if r in "SsNn":
            continuar = True
            continue
        print("\033[1;31mOpção inválida.Por favor, considere tentar novamente.\033[m")
    if r == "N":
        break


print('-=' * 60)
print(alunos)
print(f"{'Nº':<2}{'nome':>7}{'média':>14}")
print("-" * 30)
for pos, aluno in enumerate(alunos):
    print(f"{pos:<2}{aluno[0]:>7}{aluno[2]:>14}")

print('-=' * 40)

while True:
    question = 0
    while True:
        question = int(input("Mostrar as notas de qual aluno? (999 interrompe): "))
        if question < 0 or question > (len(alunos) - 1) and question != 999:
            print("\033[1;31mOpção inválida.Por favor, tente novamente.\033[m")
            continue
        break
    if question == 999:
        break
    print(f"Notas de {alunos[question][0]}: {alunos[question][1]}")

print("\033[1;32m<<< volte sempre! >>>\033[m")