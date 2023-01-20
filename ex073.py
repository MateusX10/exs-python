times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
        'Flamengo', 'Vasco', 'Chapecoence', 'Atlético', 'Botafogo',
        'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense','Sport Recife',
        'parana', 'EC Vitória', 'Curitiba', 'Avaí', 'Ponte Preta', 'atlético go')


print(f"Os 5 primeiros colocados foram: ", end='')

for time in range(0,5):
    print(f'{times[time]}, ' if time != 4 else f"{times[time]}", end='')

print("\nOs últimos 4 colocados foram: ", end='')

for time in range(len(times) - 5, len(times) - 1):
    print(f"{times[time]}, ", end='')

print(f'\nO time chapecoence está na {times.index("Chapecoence")+1}º posição ', end='')




print(f"\nTimes em ordem alfabética: {sorted(times)}")