from tv import Tv

while True:
    canal = int(input('Número do canal: '))
    if 0 < canal <= 300:
        break
    print(f'\033[1;31mERRO!Digite um canal válido!\033[m')        
while True:
    volume = int(input('Volume: '))
    if 0 <= volume <= 100:
        break
    print(f'\033[1;31mERRO!Digite um volume entre 0 e 100!\033[m')
tv1 = Tv(canal, volume)
print(f'Canal: {tv1.canal}; volume: {tv1.volume}')
while True:
    print('''Suas opções: 
[ 1 ] - Aumentar o volume
[ 2 ] - Diminuir o volume
[ 3 ] - Mudar de canal
[ 4 ] - Sair do sistema
''')
    escolha = int(input('O que quer fazer? '))
    if escolha == 1:
        tv1.aumentar()
    elif escolha == 2:
        tv1.diminuir()
    elif escolha == 3:
        tv1.MudarCanal()
    elif escolha == 4:
        break
    else:
        print('\033[1;31mERRO!Digite uma opção válida!\033[m')
    
print('\033[1;34m <<volte sempre >>\033[m')