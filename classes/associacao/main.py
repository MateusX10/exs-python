from classes import Computador, Teclado, Mouse

pc1 = Computador("PIPI", "DELL", "10GB", "I7 10580", "1024 GB")
pc2 = Computador("Altair", "ABM", "32GB", "I9", "1PB")
tec1 = Teclado()
mou1 = Mouse()


pc1.ExibirFicha()
pc2.ExibirFicha()
pc1.inserir_dado = tec1
pc1.selecionar_dado = mou1
pc1.inserir_dado.algo = "alterado"
print(pc1.inserir_dado.algo)
print(tec1.algo)
try:
    pc1.inserir_dado.digitar()
    pc1.inserir_dado.backspace()
    pc1.inserir_dado.space()
except:
    print('\033[1;31mOcorreu um erro...\033[m')
'''pc1.selecionar_dado.clicar()
pc1.selecionar_dado.rolar()
pc1.selecionar_dado.botao_direito()'''
tec1.digitar()