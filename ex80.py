numeros = list()
for n in range(1, 6):
    num = int(input('Digite um valor: '))
    if n == 1 or num > numeros[-1]:
        numeros.append(num)
        print('Valor adcionado ao final da lista')
    elif num < numeros[0]:
        numeros.insert(0, num)
        print(f'Valor adcionado na posição 0 da lista')
    else:
        pos = 0
        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos, num)
                print(f'Valor adcionado na posição {pos} da lista')
                break
            pos += 1
print(f'Valores digitados: {numeros}')

