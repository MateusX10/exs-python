n = int(input("Digite um número para ver sua tabuada: "))

for num in range(1,11):
    print(f'{n} x {num:2} = {n * num}')