s = media = nota = 0

for cont in range(0,2):
    n = float(input(f"Digite a {cont+1}º nota: "))
    s += n
media = s / 2
print(f'A média do aluno vale {media:.1f}')