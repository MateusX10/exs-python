MediaIdadeGrupo = QuantMulheresMenor20 = IdadeHomemMaisVelho =  0
NomeMaisVelho = ""
NomeMulheresMenor20 = list()

for pessoa in range(0,7):
    nome = str(input(f"Nome da {pessoa}º pessoa: ")).strip().capitalize()
    idade = int(input(f"Idade da {pessoa}º pessoa: "))
    while True:
        sexo = str(input("Sexo[M/F]: ")).strip().upper()[0]
        if sexo not in "MmFf":
            print('\033[1;31mIdade inválida.Tente novamente.\033[m')
            continue
        break
    MediaIdadeGrupo += idade
    if sexo in "Ff" and idade < 20:
        QuantMulheresMenor20 += 1
        NomeMulheresMenor20.append(nome)
    if pessoa == 1 and sexo in "Mm":
        NomeMaisVelho = nome
        IdadeHomemMaisVelho = idade
    elif idade > IdadeHomemMaisVelho and sexo in "Mm":
        NomeMaisVelho = nome
        IdadeHomemMaisVelho = idade

MediaIdadeGrupo = MediaIdadeGrupo / 4

print(f"A média da idade do grupo é {MediaIdadeGrupo:.0f} anos")
print(f"O homem mais velho tem {IdadeHomemMaisVelho} anos e se chama {NomeMaisVelho}")
print(f'''Ao todo, foram constatados um total de {QuantMulheresMenor20} mulheres
menores de 20 anos ''', end='')
for nome in NomeMulheresMenor20:
    print(f"[{nome}] ", end='')