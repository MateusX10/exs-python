from random import randint
from time import sleep


def dormir(tempo_segundos):
    sleep(tempo_segundos)



tentativas = 0
computador = randint(0,10) #Faz o computador pensar em um número
print("\033[1mOlá, jogador!Sou \033[1;32mMyint\033[m, seu computador, e pensei num número entre 0 e 10 \033[1;33m\U0001f600\033[m")
dormir(1)
print("\033[1mSerá que você consegue adivinhar em qual número eu pensei??? \033[1;33m\U0001F61B\033[m")
dormir(1)

while True:
    tentativas += 1
    while True:
        jogador = int(input("\033[1mFaça sua jogada: "))
        if jogador >= 0 and jogador < 11:
            break        
    if jogador == computador:
        break

    else:
        if jogador > computador:
            print("\033[1;33mMenos...tente novamente \033[1;31m \U0001F606 \033[m")

        else:
            print("\033[1;33mMais...tente novamente \033[1;31m \U0001F606 \033[m")
        continue

print("\033[1;31mOh, não!Como fui perder tão miseravelmente?! \033[1;33m\U0001F922\033[m")
dormir(2)
print(f"\033[1;32m[Você venceu o jogo com um total de {tentativas} tentativas]\033[m")