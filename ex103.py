def ficha(NomeJogador="<desconhecido", gols=0):
    if len(NomeJogador) == 0:
        NomeJogador = "<desconhecido>"
    print(f"O jogador {NomeJogador} fez {gols} gols no campeonato")


numero_gols = 0
nome = str(input("Nome do jogador: "))
try:
    numero_gols = int(input("Quantos gol(s)? "))
except:
    if type(numero_gols) is not int:
        numero_gols = 0


ficha(nome, numero_gols)


'''def ficha(NomeJogador="<desconhecido>", gol=0):
    print(f"O jogador {NomeJogador} fez {gol} gols no campeonato")
 


nome = str(input("Nome do jogador: "))
gols = str(input("Número de gols: "))

if gols.isnumeric():
    gols = int(gols)

else:
    gols = 0

if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)'''