from datetime import datetime

TotMaiorIdade = TotMenorIdade = 0
atual = datetime.today().year
AnosDeNascimento = list()

for p in range(0,7):
    ano_nascimento = int(input(f"Ano de nascimento da {p+1}º pessoa: "))
    AnosDeNascimento.append(ano_nascimento)
    if (atual - ano_nascimento) >= 18:
        TotMaiorIdade += 1

    else:
        TotMenorIdade += 1

for pos, ano in enumerate(AnosDeNascimento):
    print(f'{pos + 1} - {ano}')
    print(f"Idade: {atual - ano} anos")

print(f'''Ao todo, tivemos {TotMaiorIdade} pessoas maiores de idade e 
{TotMenorIdade} pessoas menores de idade''')