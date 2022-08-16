from random import randint
from time import sleep

computador = randint(0,1)
print('\033[1;33m-=' * 30)
print("\033[1;36mJOGO DA ADIVINHAÇÃO!!!\033[m".center(60))
print('\033[1;33m-=' * 30)
sleep(2)
print('\n\033[1;32mSou seu computador!')
sleep(1)
print("Pensei em um número entre 0 e 10...")
sleep(1)
print("Vamos ver se consegue acertar qual é!\033[m")
sleep(1)
jogador = int(input("\033[1mQual a sua escolha? "))
if jogador == computador:
    print('\033[1;32mParabéns!Você me venceu no meu próprio jogo :D')
    print('Eu de fato pensei no\033[1;34m número {}\033[m'.format(computador))
else:
    print('\033[1;31mOps, parece que não foi desta vez... melhor na próxima :)')
    print(f'Eu pensei no\033[1;35mnúmero {computador}\033[1;31m não no\033[1;34mnúmero {jogador}\033[m')