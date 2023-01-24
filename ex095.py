player = dict()
players = list()
gols = list()
GamesPlayedByPlayer = choice = 0
answer = ' '
while True:
    player["nome"] = str(input("\033[mPlayer's name: "))
    GamesPlayedByPlayer = int(input(f"How many games the player {player['nome']} played? "))
    for GamePlayed in range(0,GamesPlayedByPlayer):
        gols.append(int(input(f"How many gols did you do in the {GamePlayed+1}º game?")))
    player["gols"] = gols[:]
    player["total"] = sum(player["gols"])

    players.append(player.copy())
    gols.clear()


    while True:
        answer = str(input("Continue [Y/N]? ")).strip().upper()[0]
        if answer in "YN":
            break
        print('\033[1;31mERROR!Please, try again.\033[m')
    
    if answer == 'N':
        break


print(players)

print(f"{'cod'}", end='')
for i in player.keys():
    print(f'{i:<17}', end='')

print()

for i, player in enumerate(players):

    print(f"\n{i:>4}", end='')
    for dado in player.values():
        print(f'{str(dado):<17}', end='')

s
while True:
    
    choice = int(input('\nShow the data of which players? (type 999 to stop) '))
    if choice == 999:
        break
    if choice >= len(players) and choice != 999:
        print(f'\033[1;31mERROR!This is no a player with code "{choice}"!\033[m')
    else:
        print(f"\033[1;34m<<< {players[choice]['nome']} player data >>>\033[m")
        print('-=' * 40)
        for i, v in enumerate(players[choice]['gols']):
            print(f"In match {i+1} he scored {v} goals")


print("\033[1;32m<<< Finished program >>> \033[m")