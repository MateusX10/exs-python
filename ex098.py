from time import sleep

def line():
    print('-=' * 30)
def contador(ini, fim, passo):
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1
    print(f'Contagem de {ini} até {fim} pulando de {passo} em {passo}')
    cont = ini
    if ini < fim:
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont += passo
    else:
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont -= passo
    print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a sua contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)