num = str(input("Digite um número de 0 a 9999: "))
lista_num = []
for numero in num:
    lista_num.append(numero)

while len(lista_num) < 4:
    lista_num.insert(0, 0)

print(f'''Unidade: {lista_num[-1]} \nDezena: {lista_num[-2]} \nCentena: {lista_num[-3]}
Milhar: {lista_num[-4]}''')
    