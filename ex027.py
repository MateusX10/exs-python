nome = str(input("Seu nome completo: ")).strip().capitalize()


print(f'Muito prazer em te conhecer, {nome}!')
nome = nome.split()
print(f'Seu primeiro nome é {nome[0]} e seu último nome é {nome[-1]}')