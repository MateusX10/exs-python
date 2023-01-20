from random import randint
from time import sleep
from operator import itemgetter


corredores = {"corredor1": randint(15, 40),
              "corredor2": randint(15,40),
              "corredor3": randint(15,40),
              "corredor4": randint(15,40),
              "corredor5": randint(15,40)
              }

for k, v in corredores.items():
    print(f"{k} correu a {v} Km/h")
    sleep(1)

print(corredores)

ranking = list()


ranking = sorted(corredores.items(), key=itemgetter(1), reverse=True)

print("\033[1;32m=== RANKING: ===\033[m")

for pos, v in enumerate(ranking):
    print(f"{pos+1}º posição: {v[0]} atingindo {v[1]}Km/h")
    sleep(1)
