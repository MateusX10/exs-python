numeros = (int(input('Digite um valor: ')),
          int(input('Digite mais um valor: ')),
          int(input('Digite outro valor: ')),
          int(input('Digite um último valor: ')))

print(f'Você digitou os seguintes valores: {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}º posição')
else:
    print('\033[1;31mNão encontrei o valor 3...\033[m')
print('Os valores pares digitados foram ', end='')
for valor in numeros:
    if valor % 2 == 0:
        print(f'{valor} ', end='')