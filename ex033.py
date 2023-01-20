'''numeros = list()

for n in range(0,3):
    num = int(input(f"{n+1}º valor: "))
    numeros.append(num)

print(f'O maior valor digitado foi {max(numeros)} \nO menor valor digitado foi {min(numeros)}')'''

maior = menor = 0

for num in range(1,4):
    n1 = int(input(f"Digite o {num}º valor: "))
    if num == 1:
        maior = menor = n1

    if n1 > maior:
        maior = n1

    if n1 < menor:
        menor = n1

print(f'O maior valor digitado foi {maior} e o menor {menor}')

    


