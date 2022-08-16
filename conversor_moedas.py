from time import sleep

while True:
    try:
        reais = float(input('\033[1;36m -->\033[m \033[1mQuanto dinheiro você tem na carteira? R$'))

    except (ValueError, TypeError): # Mensagem de erro
        print(f'\n\033[1;36m -->\033[m \033[1;31mTivemos um problema com o tipo de dados que você informou.Tente novamente\033[m')
        sleep(1)

    except (KeyboardInterrupt):  #sai do programa quando o usuário interrompe a entrada de dados
        print('\n\033[1;36m --> \033[1;33mO usuário preferiu não informar os dados\033[m')
        print(' \033[1;36m--> \033[1;34m<<< \033[mVolte sempre :D\033[34m >>>\033[m')
        quit() # Sai do programa
    else:
        break
dolar = reais / 5.18
euro = reais / 5.28
iene = reais * 26.02
libra = reais / 6.27
remimbi_yuam = reais * 1.30
print(f'\n\033[1;36m -->\033[m \033[1mCom \033[1;32mR${reais:.2f}\033[m \033[1m(moeda BR), você pode comprar \n\n   \033[1;35m>>\033[m \033[1;32mUS${dolar:.2f}\033[m \033[1m(moeda americana/EUA) \n\n   \033[1;35m>>\033m \033[32m{euro:.2f}£\033[m \033[1m(euro) \n\n   \033[1;35m>>\033[m \033[1;32m¥{iene:.2f}\033[m \033[1m(moeda japonesa) \n\n   \033[1;35m>>\033[m \033[1;32m{libra:.2f} £\033[m \033[1m(moeda inglesa) \n\n   \033[1;35m>>\033[m \033[1;32m¥{remimbi_yuam:.2f}\033[m \033[1m(moeda chinesa)\033[m')
#Imprime na tela a moeda convertida para dólar, euro, iene, libra e remimbi/yuam