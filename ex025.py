nome = str(input("Nome: ")).title().strip()

if "SANTO" in nome.upper():
    print(f'\033[1;32mO nome {nome} TEM SANTO no meio!\033[m')
else:
    print(f'\033[1;31mO nome {nome} NÃO TEM SANTO no meio!\033[m')

print(f'Seu nome tem silva? {"SILVA" in nome.upper()}')