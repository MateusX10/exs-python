nome = str(input("Digite seu nome compĺeto: ")).strip().capitalize()

print(f'Seu nome em maiúsculas é {nome.upper()} \nSeu nome em minúsculas é {nome.lower()}')

print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
print(f'Seu 1º nome tem {nome.find(" ")} letras')
print(f'Seu último nome tem ao todo {len(nome) - (nome.rfind(" ") + 1)} letras')