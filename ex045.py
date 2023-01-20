from random import choice
from time import sleep


def MostraMenu():

    print('''Suas opções:
    [ 1 ] - PEDRA
    [ 2 ] - PAPEL
    [ 3 ] - TESOURA
    ''')


opcs = ['pedra', 'papel', 'tesoura']

computador = choice(opcs)


MostraMenu()
jogador = int(input("Sua jogada: ")) - 1
jogador = opcs[jogador]


print("\033[1;32mJO")
sleep(1)
print("KEN")
sleep(1)
print('PÔ!\033[m')
sleep(1)

print(f"Computador joga {computador}")
sleep(1)
print(f"Jogador joga {jogador}")
sleep(1)
if jogador == computador:
    print("\033[1;33mEMPATE!\033[m")
 
elif jogador == "pedra" and computador == "tesoura" or jogador == "tesoura" and computador == "papel" or jogador == "papel" and computador == "pedra":
    print("\033[1;32mVocê venceu!\033[m")

elif computador == "pedra" and jogador == "tesoura" or computador == "tesoura" and jogador == "papel" or computador == "papel" and jogador == "pedra":
    print("\033[1;31mVocê perdeu!\033[m")