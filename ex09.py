from time import sleep


num = int(input('Digite um número para ver sua tabuada: '))
print(f'\033[1;32mA mostrar tabuada do {num}...\033[m')
sleep(1)
for cont in range(1,11):
    print(f'{num} x {cont:2} = {num * cont}')
print("fim")