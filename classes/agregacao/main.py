from computador import Pc, Teclado, Mouse

comandos_tec = []
comandos_mouse = []
pc1 = Pc()

com1 = Teclado("ctrl + c")
com2 = Teclado("ctrl + v")
com3 = Teclado("ctrl + z")
com4 = Teclado("f5")
com5 = Teclado("ctrl + a")
comouse1 = Mouse("botão direito")
comouse2 = Mouse("botão esquerdo")
comouse3 = Mouse("rolar para baixo")
comouse4 = Mouse("rolar para cima")
comandos_tec = [com1, com2, com3, com4, com5]
comandos_mouse = [comouse1, comouse2, comouse3, comouse4]
for c in comandos_tec:
    pc1.digitar_comando(c)
for c in comandos_mouse:
    pc1.digitar_comando(c)
pc1.listar_comandos()
pc1.comandos_tot()


