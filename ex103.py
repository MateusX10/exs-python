def line():
    print('-=' * 30)
def ficha(jogador='<desconhecido>', gols=0):
    print(f'Jogador {jogador} fez {gols} gols no campeonato')


nome = str(input('Nome do jogador: ')).strip()
gol = str(input('Número de gols: '))
if not gol.isnumeric():
    gol = 0
else:
    gol = int(gol)
if nome == '':
    ficha(gols=gol)
else:
    ficha(nome, gol)
