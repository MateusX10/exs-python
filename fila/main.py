from funcs import *
from time import sleep


fila = []
valor = SomaItensFila = TotItensAdicionados = TotItensRemovidos = 0
opcs = ["Adicionar itens na fila", "Remover itens da fila", "Mostrar itens da fila", "sair"]

while True:
    tamanho_fila = leiaInt("Qual o tamanho da fila? ")
    if tamanho_fila == 0:
        print("\033[1;31mTamanho da fila deve ser diferente de 0\033[m")
        continue
    break
print(f"\033[1;32mFila de tamanho {tamanho_fila} definido com sucesso\033[m")


while True:
    LimpaTela()
    escolha = Menu(opcs)
    
    
    if escolha == 1:
        try:
            valor = AdicionaItemNaFila(fila, tamanho_fila)
            TotItensAdicionados += 1
            SomaItensFila += valor
        except:
            pass
    
    elif escolha == 2:
       valor = RemoveItensDaFila(fila)
       if valor:
           TotItensRemovidos += 1


    elif escolha == 3:
        ListaElementosDaFila(fila)

    elif escolha == 4:
        break

sleep(2)
LimpaTela(False)
print(f"Ao todo, foram adicionados {TotItensAdicionados} itens na fila")
print(f"A soma de todos os itens adicionados na  fila foi {SomaItensFila}")
print(f"No total, foram removidos {TotItensRemovidos} itens na lista")
print('-=' * 30)
print("\033[1;33m<<< \033[1;32mVolte sempre!\033[1;33m >>>\033[m")
