jogador = dict()
gols = list()

jogador["nome"] = str(input("Nome do jogador: "))
QuantPartidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

for partida in range(0,QuantPartidas):
    gols.append(int(input(f"Quantos gols na partida {partida+1}? ")))

jogador["gols"] = gols.copy()
jogador["total"] = len(gols)
print('-=' * 40)
print(jogador)
print('-=' * 40)
for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")

print(f"O jogador {jogador['nome']} jogou {jogador['total']} partidas")

for k in jogador.keys():
    for pos, v in enumerate(k[1]):
        print(f"Na {pos+1} partida, o jogador {jogador['nome']} fez {v} gols")


