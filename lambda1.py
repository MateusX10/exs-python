# def area(larg, comp):
#     return larg * comp

# comp = float(input("Comprimento do terreno: "))
# larg = float(input("Largura do terreno: "))

# result = area(larg, comp)
# print(f'A área de um terreno de {larg}X{comp} é de {result}')

area = lambda larg, comp: larg * comp

comp = float(input("Comprimento do terreno: "))
larg = float(input("Largura do terreno: "))

print(f'A área de um terreno {larg}X{comp} vale {area(larg, comp)}')

