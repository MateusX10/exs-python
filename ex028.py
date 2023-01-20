from random import randint

def linha():
    print("-=" * 40)

computador = randint(0,5)

linha()
print("\033[1;32mVou pensar em um número entre 0 e 5...Vamos ver se consegue acertar!\033[m")
linha()

jogador = int(input("Sua escolha: "))

if jogador == computador:
    print("\033[1;32mVocê venceu!\033[m")
else:
    print("\033[1;31mVocê perdeu!\033[m")