from time import sleep
nome = str(input('Nome completo: ')).strip()
print('Analisando o seu nome...')
sleep(1)
print(f'Seu nome em maiúsculas é {nome.upper()}\nSeu nome em minúsculas é {nome.lower()}')
junto = nome.split()
junto = "".join(junto)
print(f'Seu nome tem ao todo {len(junto)} letras')
primeiro = nome.split()[0]
print(f'Seu primeiro nome é {primeiro} e ele tem {len(primeiro)} letras')