nome = str(input("Nome: ")).strip().title()

separado = nome.split() #separa o nome da pessoa
primeiro = separado[0] #pega o primeiro nome
ultimo = separado[len(separado) - 1] #pega o último nome
print(f"É um prazer conhecê-lo, \033[1;32m{nome}\033[m!")
print(f'''Seu primeiro nome é \033[1;32m{primeiro}\033[m \nSeu último nome é \033[1;32m{ultimo}\033[m''')
#printa o primeiro e o último nome do indivíduo