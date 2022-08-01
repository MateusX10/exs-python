princ = []
dado = []
while True:
    dado = [str(input('Nome: '))]
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    média = (nota1 + nota2) / 2
    dado.append(média)
    dado.append([nota1, nota2])
    princ.append(dado[:])
    dado.clear()
    while True:
        r = str(input('Continuar? [S/N]')).strip().upper()[0]
        if r in "SN":
            break
        print(f'\033[1;31m"{r}" é um opção inválida.Digite somente "S" ou "N!\033[m')
    if r == "N":
        break
print(princ)
print('-='*30)
print(f'{"Nº":<14}{"NOME":<10}{"MÉDIA":>6}')
for pos, v in enumerate(princ):
    print(f'{pos:<14}{princ[pos][0]:<10}{princ[pos][1]:>6.2f}')

while True:
    while True:
        escolha = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
        if len(princ) > escolha >= 0 or escolha == 999:
            break
    print('-=' * 30)
    if escolha == 999:
        print('Finalizando...')
        break
    else:
        print(f'Notas de {princ[escolha][0]} são {princ[escolha][2]}')
print('Volte sempre ;D')
